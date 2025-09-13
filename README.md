# Lemmatization tool based on pymorphy3 and spacy

# Get started
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

-------------------------
A small note. pymorphy2 does not support python 3.12, so pymorphy3 is used. 
PorterStemmer is not suitable for checking the Russian language, so SnowballStemmer is used for Russian.

And, in general, we can not check pymorphy3 and spacy with PorterStemmer.
PorterStemmer is used for stemming, but according to instructions we use pymorphy3 and spacy for lemmatization, it is quite different things.
------------------------

# Example
```
English words:
----------------------------------------------------------------------
word                   spacy                  PorterStemmer         
----------------------------------------------------------------------
running                run                    run                   
jumped                 jump                   jump                  
better                 well                   better                
happiest               happy                  happiest              
studies                study                  studi                 
mice                   mouse                  mice                  
was                    be                     wa                    
are                    be                     are                   

Russian words:
----------------------------------------------------------------------
word                   pymorphy3              SnowballStemmer       
----------------------------------------------------------------------
бежавший               бежать                 бежа                  
стоял                  стоять                 стоя                  
лучше                  хороший                лучш                  
счастливейший          счастливый             счастлив              
учусь                  учиться                уч                    
мыши                   мышь                   мыш                   
был                    быть                   был                   
есть                   есть                   ест                   
```