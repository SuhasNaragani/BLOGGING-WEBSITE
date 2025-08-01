from celery import shared_task
import time

@shared_task
def post_published_notification(post_id, post_title):
    # Simulate a time-consuming task like sending an email
    print(f"Starting notification task for post '{post_title}' (ID: {post_id})...")
    time.sleep(5) # Simulate 5-second network delay
    # In a real app, you would log this to a database table.
    print(f"Notification sent and event logged for post '{post_title}'.")
    return "Task completed."