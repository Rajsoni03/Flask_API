# Flask API
Flask API using JWT and set the request limit

## The Task
#### Build a flask api along with a basic 2 page interface, which has the following functionality: 
1. Simple interface to upload images and when you click "submit" button, it shows a new page with name of the uploaded image.
2. Build a key based authentication system using JWT token for accessing the api functionality.
3. Put in place a throttle for api call rate, 5/min.


## Uses

**Step 1. -** Install all requirements using this command
```Batchfile
>> pip install -r requirements.txt
```

**Step 2. -** Open terminal and use following command for run the project<br>
```Batchfile
>> python main.py
```

**Step 3. -** Open browser and type url:<br>
http://127.0.0.1:5000<br>
http://127.0.0.1:5000/token<br>
http://127.0.0.1:5000/api?token=YOUR_TOKEN<br>
