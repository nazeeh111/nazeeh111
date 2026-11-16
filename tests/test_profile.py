"""Broken-profile controls against a fresh copy of the real profile."""

import hashlib
import importlib.util
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('profile_check', ROOT / 'scripts/check_profile.py')
checker = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checker)


class ProfileTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='profile-integrity-')
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        for name in ('README.md', 'START_HERE.md', 'profile-assets.json'):
            shutil.copyfile(ROOT / name, self.root / name)
        shutil.copytree(ROOT / 'assets', self.root / 'assets')

    def replace(self, name, old, new):
        path = self.root / name
        content = path.read_text()
        self.assertIn(old, content)
        path.write_text(content.replace(old, new))

    def refused(self, text):
        self.assertTrue(any(text in error for error in checker.check(self.root)))

    def test_real_profile_from_another_working_directory_no_writes(self):
        def hashes():
            return {p.relative_to(self.root).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
                    for p in self.root.rglob('*') if p.is_file()}
        before = hashes()
        result = subprocess.run([sys.executable, '-I', str(ROOT / 'scripts/check_profile.py'),
                                 '--root', str(self.root)], cwd='/tmp', capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(hashes(), before)

    def test_missing_responsive_image(self):
        (self.root / 'assets/solidrift-comparison-mobile.svg').unlink()
        self.refused('missing')

    def test_unmapped_new_image(self):
        self.replace('README.md', 'assets/solidrift-comparison.svg', 'assets/missing-body-light.svg')
        self.refused('image/provenance map differs')

    def test_missing_provenance(self):
        (self.root / 'assets/solidrift-comparison-provenance.md').unlink()
        self.refused('missing')

    def test_mutable_source_link(self):
        self.replace('START_HERE.md', '/blob/1902168d1c6d64a448434e78dfe5ad840360093a/', '/blob/main/')
        self.refused('full40hex')

    def test_nested_provenance_source_checked(self):
        self.replace('assets/missing-body-provenance.md', '/blob/8fc9e23471a18165d73646e290700cc10d351eea/', '/blob/main/')
        self.refused('full40hex')

    def test_local_escape_refused(self):
        self.replace('START_HERE.md', '[All projects]', '[outside](../outside.md)\n\n[All projects]')
        self.refused('escapes repository')

    def test_symlink_escape_refused(self):
        (self.root / 'outside.md').symlink_to(ROOT / 'README.md')
        self.replace('START_HERE.md', '[All projects]', '[outside](outside.md)\n\n[All projects]')
        self.refused('escapes repository')

    def test_mobile_description_required(self):
        self.replace('assets/solidrift-comparison-mobile.svg', '<desc id="mobile-description">', '<metadata id="mobile-description">')
        self.replace('assets/solidrift-comparison-mobile.svg', '</desc>', '</metadata>')
        self.refused('root desc')

    def test_accessible_label_must_resolve(self):
        self.replace('assets/solidrift-comparison-mobile.svg', 'mobile-title mobile-description', 'mobile-title mobile-description absent')
        self.refused('missing id')

    def test_invalid_provenance_type_is_a_diagnostic(self):
        data = json.loads((self.root / 'profile-assets.json').read_text())
        data['images']['assets/solidrift-comparison.svg'] = 17
        (self.root / 'profile-assets.json').write_text(json.dumps(data))
        self.refused('must be a string')

    def test_generator_reproduces_both_current_svgs(self):
        subprocess.run([sys.executable, str(self.root / 'assets/build-solidrift-figure.py')], check=True)
        for name in ('solidrift-comparison.svg', 'solidrift-comparison-mobile.svg'):
            self.assertEqual((self.root / 'assets' / name).read_bytes(), (ROOT / 'assets' / name).read_bytes())

    def test_all_title_forms_check_targets_and_revisions(self):
        for title in ('"double title"', "'single title'", '(parenthesized title)'):
            with self.subTest(title=title):
                refs, _ = checker.references(f'[broken](missing.md {title})')
                self.assertEqual(refs, [('missing.md', False)])
                self.assertFalse(checker.immutable_source('https://github.com/nazeeh111/test/blob/main/source.py'))
                with (self.root / 'START_HERE.md').open('a') as stream:
                    stream.write(f'\n[broken](missing.md {title})\n')
                self.refused('missing')

    def test_angle_balanced_and_escaped_destinations(self):
        for syntax, filename in [('<present file.md>', 'present file.md'),
                                 ('present(2).md', 'present(2).md'),
                                 (r'present\(2\).md', 'present(2).md')]:
            with self.subTest(syntax=syntax):
                (self.root / filename).write_text('Present file.')
                refs, _ = checker.references(f'[present]({syntax})')
                self.assertEqual(refs, [(filename, False)])
                with (self.root / 'START_HERE.md').open('a') as stream:
                    stream.write(f'\n[present]({syntax})\n')
                self.assertEqual(checker.check(self.root), [])


if __name__ == '__main__':
    unittest.main()
