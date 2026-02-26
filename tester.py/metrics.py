def analyze(stream):
    for event in stream:
        if event["value"] > 100:
            print("Anomaly detected")
