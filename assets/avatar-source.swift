import AppKit

let size: CGFloat = 500
let image = NSImage(size: NSSize(width: size, height: size))
image.lockFocus()

NSColor(calibratedRed: 0.050, green: 0.094, blue: 0.133, alpha: 1).setFill()
NSBezierPath(rect: NSRect(x: 0, y: 0, width: size, height: size)).fill()

// A quiet calibration grid remains visible at full size, not at avatar size.
NSColor(calibratedRed: 0.13, green: 0.22, blue: 0.27, alpha: 1).setStroke()
for coordinate in stride(from: CGFloat(50), through: CGFloat(450), by: CGFloat(50)) {
    let vertical = NSBezierPath()
    vertical.move(to: NSPoint(x: coordinate, y: 0))
    vertical.line(to: NSPoint(x: coordinate, y: size))
    vertical.lineWidth = 1
    vertical.stroke()
    let horizontal = NSBezierPath()
    horizontal.move(to: NSPoint(x: 0, y: coordinate))
    horizontal.line(to: NSPoint(x: size, y: coordinate))
    horizontal.lineWidth = 1
    horizontal.stroke()
}

let n = NSBezierPath()
n.move(to: NSPoint(x: 122, y: 128))
n.line(to: NSPoint(x: 122, y: 372))
n.line(to: NSPoint(x: 378, y: 128))
n.line(to: NSPoint(x: 378, y: 372))
n.lineWidth = 45
n.lineCapStyle = .round
n.lineJoinStyle = .round
NSColor(calibratedRed: 0.94, green: 0.97, blue: 0.98, alpha: 1).setStroke()
n.stroke()

let signal = NSBezierPath()
signal.move(to: NSPoint(x: 65, y: 250))
signal.line(to: NSPoint(x: 145, y: 250))
signal.curve(to: NSPoint(x: 195, y: 250), controlPoint1: NSPoint(x: 170, y: 250), controlPoint2: NSPoint(x: 175, y: 319))
signal.curve(to: NSPoint(x: 235, y: 250), controlPoint1: NSPoint(x: 210, y: 181), controlPoint2: NSPoint(x: 220, y: 250))
signal.line(to: NSPoint(x: 435, y: 250))
signal.lineWidth = 10
signal.lineCapStyle = .round
NSColor(calibratedRed: 0.40, green: 0.84, blue: 0.91, alpha: 1).setStroke()
signal.stroke()

NSColor(calibratedRed: 0.97, green: 0.78, blue: 0.40, alpha: 1).setFill()
NSBezierPath(ovalIn: NSRect(x: 414, y: 239, width: 22, height: 22)).fill()

image.unlockFocus()
guard let tiff = image.tiffRepresentation,
      let bitmap = NSBitmapImageRep(data: tiff),
      let png = bitmap.representation(using: .png, properties: [:]) else {
    fatalError("Could not render avatar")
}
let outputPath = CommandLine.arguments.dropFirst().first ?? "assets/avatar.png"
try png.write(to: URL(fileURLWithPath: outputPath))
