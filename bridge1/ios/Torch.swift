import Foundation
import AVFoundation

@objc(Torch)
class Torch: NSObject {
  
  @objc
  func on(){
    toggleTorch(on: true)
    print("PRINTED SOMETHING")
  }
  
  @objc
  func off(){
    toggleTorch(on: false)
  }
  
  private func toggleTorch(on: Bool) {
      guard
          let device = AVCaptureDevice.default(for: AVMediaType.video),
          device.hasTorch
      else { return }

      do {
          try device.lockForConfiguration()
          device.torchMode = on ? .on : .off
          device.unlockForConfiguration()
      } catch {
          print("Torch could not be used")
      }
  }
}
