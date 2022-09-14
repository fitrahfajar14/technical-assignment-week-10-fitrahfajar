from ultrasonic import distance
import requests
import time

# ultrasonic 1
gpio_echo_1 = 1
gpio_trigger_1 = 2
device_label_1 = 'ultrasonic_1'
device_token_1 = 'BBFF-xPHGGSOJUxeuh8Ijbz39FYaTdZFFSd'

# ultrasonic 2
gpio_echo_2 = 4
gpio_trigger_2 = 5
device_label_2 = 'ultrasonic_2'
device_token_2 = 'BBFF-lTM2PEeMrd9fpm1Y2uITnxUUUhtTqg'


def send_to_ubidots(device_label, device_token, payload):
    # Creates the headers for the HTTP requests
    url = "http://industrial.api.ubidots.com"
    url = "{}/api/v1.6/devices/{}".format(url, device_label)
    headers = {"X-Auth-Token": device_token, "Content-Type": "application/json"}

    # Makes the HTTP requests
    status = 400
    attempts = 0
    while status >= 400 and attempts <= 5:
        req = requests.post(url=url, headers=headers, json=payload)
        status = req.status_code
        attempts += 1
        time.sleep(1)

    # Processes results
    print(req.status_code, req.json())
    if status >= 400:
        print("[ERROR] Could not send data after 5 attempts, please check \
            your token credentials and internet connection")
        return False

    print("[INFO] request made properly, your device is updated")
    return True



if __name__ == "__main__":
    while True:
        # sensor 1 reading
        distance_1 = distance(gpio_trigger_1, gpio_echo_1)
        distance_1_payload = {
            'ultrasonic': distance_1
        }
        send_to_ubidots(device_label_1, device_token_1, distance_1_payload)
        
        # tambahan logic misal jarak tertentu menyalakan/matikan relay atau servo

        # sensor 2 reading
        distance_2 = distance(gpio_trigger_2, gpio_echo_2)
        distance_2_payload = {
            'ultrasonic': distance_2
        }
        send_to_ubidots(device_label_2, device_token_2, distance_2_payload)

        # tambahan logic misal jarak tertentu menyalakan/matikan relay atau servo
