import time
from naoqi import ALProxy

def track(track_duration=10):
    motion_service = ALProxy("ALMotion", "127.0.0.1", 9559)
    tracker_service = ALProxy("ALTracker", "127.0.0.1", 9559)
    # First, wake up.
    motion_service.wakeUp()
    # Add target to track.
    targetName = "Face"
    tracker_service.registerTarget(targetName, 0.1)
    # Then, start tracker.
    tracker_service.track(targetName)

    # Sleep during tracking time
    time.sleep(track_duration)

    # Stop tracker.
    tracker_service.stopTracker()
    tracker_service.unregisterAllTargets()
    motion_service.rest()

try:
    trackerBot = Tracker()
except BaseException, err:
    print err
