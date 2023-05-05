# dataconv


This is a small project created to automate email extraction from csv and xlsx file

## What does it do actually???

- Suppose, Person A have csv/excel file which have email address column
- Now, he want to extract all the email addresses of that column
- What will he do is upload that file `upload/` endpoint and send a POST request
- This app will search the email column, process it, write it to the database and will return all processed email addresses as a response



## Set up

1. Clone the project `git clone https://github.com/chapainaashish/dataconv/`
   

2. Create a virtual environment and install dependencies `pipenv install`
   

3. Enter into a virtual environment `pipenv shell`
   

4. Run the server `python manage.py runserver`
   

5. Go to `http://127.0.0.1:8000/upload` 


6. Upload the email file `csv` or `xlsx`


