# Projects-rating

This project was generated with [Python](https://github.com/python) version 3.7.8 Django 3.0.8
  
#### This is a python projects rating application. Current version 2020
</table>
</tr>
</td>

#### By **Kingsleymuturi**
  
## Description of functionality:
This app enables users to view various projects by other users and give them a rating having an option to also post projects once the user creates an account.The user can also view other user profiles along with how many projects the user has.
## Access
* Click this link to access the web app https://project-rating.herokuapp.com/

## How to run the application locally
To get the code..

1. Cloning the repository:
  ```bash
  git clone https://github.com/Kingsleymuturi/Projects-rating.git
  ```
2. Move to the folder and install requirements
  ```bash
  cd Projects-rating
  pip install -r requirements.txt
  ```
3. Create a .env file and add it to gitignore then add the following in it.
  ```bash
  SECRET_KEY='<insertsecretkey>'
  DEBUG=True 
  DB_NAME='<insert database name>'
  DB_USER='<insert database username>'
  DB_PASSWORD='<insert database password>'
  DB_HOST='127.0.0.1'
  MODE='dev'
  ALLOWED_HOSTS='.localhost', '.herokuapp.com', '.127.0.0.1'
  DISABLE_COLLECTSTATIC=1
  ```
4. Running the application
  ```bash
  python3 manage.py runserver
  ```
Open the application on your browser `127.0.0.1:8000`.

## Known Bugs
There are no known bugs yet. Feel free to inform me if you find one via my email provided below!
### Development
Want to contribute? Great!

To fix a bug or enhance an existing module, follow these steps:

- Fork the repo
- Create a new branch (`git checkout -b improve-feature`)
- Make the appropriate changes in the files
- Add changes to reflect the changes made
- Commit your changes (`git commit -m 'Improve feature'`)
- Push to the branch (`git push origin improve-feature`)
- Create a Pull Request 

## Technologies Used
During the creation of this webpage I used Python(Django).
## Support and contact details
In case of anything find me here: kingsleymuturi9@gmail.com feel free to communicate any issue with the webpage

### [LICENSE](https://github.com/Kingsleymuturi/Projects-rating/blob/master/LICENSE)
Copyright (c) 2020 [Kingsley Muturi ](https://github.com/Kingsleymuturi)
