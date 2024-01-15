from prefect import task, flow

@task
def hello_world():
    return 'Hello world'

@task
def weather_report(temp):
    if temp >= 80:
        return  'it is hot out today'
    elif 60 <= temp < 80:
        return 'it is nice out today'
    elif 50 <= temp < 60:
        return 'it is chilly out today'
    else:
        return 'it is cold out today'

@flow()
def today():
    greeting = hello_world()
    weather = weather_report(65)
    print(greeting + ', ' + weather)

if __name__ == "__main__":
    today()
