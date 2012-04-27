Twitter Spell Checking
=======

Installation
------------
```bash
python setup.py install
```

Configuration
-------------

Create a conf file as this one : 

```
[twitter]
CONSUMER_KEY = gFlXceJo9HKBeZjXOjgw
CONSUMER_SECRET = QpCq1uQLsBC3FvreKMqzkfKUllf0R22LM6oCP50
ACCESS_TOKEN = 195869-eTemy6p0ljmq2cWL6kGTXTR1BT7BpJqX9uNwzftpo
ACCESS_TOKEN_SECRET = kfAcMwqrJ9sEUjwy1vf0ItL7Nf673DBEnTCLvaM

[namespace:fr]
files = /var/www/twitter_spelling/
accounts = Caradisiac, gizmodofr, Rue89, futurasciences, purecharts, jeuxvideo, LeNouvelObs, sports_direct, 20minutes, SportF24, Slatefr, PremiereFR, LaRedouteFR, liberation_info, purepeople, Maxisciences, aufeminin_com, ZDNet, AutoPlus, lequipe, lemondefr, Telerama, Clubic, GEOfr, lesinrocks, France24_fr, LesEchos, doctissimo, ELLEfrance,  Boursier_com, francefootball

[namespace:en]
files = /var/www/twitter_spelling/
accounts = Slate, gizmodo
```


Fetch the tweets
-------------

```
twitter_spelling fetch -n [namespace] -c [settings_file_location]
```

The tweets will be loggued into the file [files]/tweets_[namespace].txt

Spell Checking
-------------

Some parts of code from http://norvig.com/spell-correct.html

```
from twitter_spelling import Correct
c = Correct(settings_file_location)
c.correct('my expression')
```

If in your namespace, your are following some sport and news account :

```
>> c.correct('franck riberi')
franck ribery
>> c.correct('steve job')
steve jobs
```
