import sentry_sdk

sentry_sdk.init(
    dsn="https://your-sentry-dsn@sentry.io/your-project-id",
    traces_sample_rate=1.0
)

def faulty_function():
    1 / 0  # This will cause an error

if __name__ == "__main__":
    try:
        faulty_function()
    except Exception as e:
        sentry_sdk.capture_exception(e)
