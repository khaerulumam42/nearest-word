export fileid=1HDMzbxacvU7-8pJuiFXGstw1gtBIYNZ9
export filename=models/wiki_skipgram.vec

if [ -f $filename ]
  then
  echo "$filename exists"
else
  mkdir models

  ## WGET ##
  wget --save-cookies cookies.txt 'https://docs.google.com/uc?export=download&id='$fileid -O- \
     | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1/p' > confirm.txt

  wget --load-cookies cookies.txt -O $filename \
     'https://docs.google.com/uc?export=download&id='$fileid'&confirm='$(<confirm.txt)
  
fi

# https://drive.google.com/file/d/1HDMzbxacvU7-8pJuiFXGstw1gtBIYNZ9/view?usp=sharing
