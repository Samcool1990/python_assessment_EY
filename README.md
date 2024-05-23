Python 3.11.0 should be installed on system  

1. Go to proper directory & open git bash/command line
2. type command "git clone 'Http address of the repo'"
3. open the cloned repo in vs code/ide
4. open terminal (Its should be location of your current project folder) 
5. type command "pip install -r requirements.txt" in terminal
6. type command "uvicorn app.main:app --reload" 
7. default localhost will open & click on it
8. now go to postman given the url: http://127.0.0.1:8000/add method as POST & below body
   {
    "batchid": "id0101",
    "payload": [[1,2],[5,2]]
}

Response will be as expected:
{
    "batchid": "id0101",
    "response": [
        3,
        7
    ],
    "status": "complete",
    "started_at": "2024-05-23T13:00:17.416702",
    "completed_at": "2024-05-23T13:00:17.711082"
}

