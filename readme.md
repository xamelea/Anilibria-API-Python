# Python library for Anilibria v3.0 API
##### **BE CAREFUL!!!**
newbie wrote this library

### [docs for Anilibria v3.0 API](https://github.com/anilibria/docs/blob/master/api_v3.md)
## Structure
this repository has a two parts:
1. Examples of code (lazy priority)
2. Library in [anilibriaAPI3 folder](https://github.com/xamelea/AnilibriaAPIv3Python/tree/master/anilibriaAPI3)(main priority)
## [api.py](https://github.com/xamelea/AnilibriaAPIv3Python/blob/master/anilibriaAPI3/api.py)
This file contains main methods to do main activities :3
## [auth.py](https://github.com/xamelea/AnilibriaAPIv3Python/blob/master/anilibriaAPI3/auth.py)
This file contains main method `auth()` that makes(verifying) authorization and creating *"session"* file
#### *Session* file
This file creates after use `auth()` method and contains **sessionId** and **cookie name** for check session expiring status
## [config.py](https://github.com/xamelea/AnilibriaAPIv3Python/blob/master/anilibriaAPI3/config.py)
Thiiis file contains all your personal info ^_^
`url` - URL for main API requests
`mail` - your email in Anilibria account
`password` - your password in Anilibria account
!!!`auth_url` - this url for login page (main page is `https://anilibria.tv/public/login.php`), but for people in countries where main Anilibria URL was blocked I advise to use mirror URL. To get mirror URL visit [iss.one/al](https://iss.one/al). Don't forget put in `auth_url` mirror URL in this `{mirror_url}/public/login.php` format.
# 
