def get_clicks(actual_time, desired_time):
  desired_hour, desired_minute = desired_time.split(":")
  actual_hour, actual_minute = actual_time.split(":")
  number_hours = int(desired_hour) - int(actual_hour)
  number_minutes = int(desired_minute) - int(actual_minute)
  number_clicks = number_hours * 12 + number_minutes / 5
  return int(number_clicks)