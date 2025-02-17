class Notifier:
    def __init__(self, threshold: float):
        self.threshold = threshold

    def check_threshold(self, value: float) -> bool:
        if value > self.threshold:
            print(f"Alert! {value} exceeded the threshold {self.threshold}")
            return True
        return False
