# Snake GIF from your GitHub contribution calendar history :snake:
<div align="center">
  <img  src="https://github.com/solomspd/contribution-cal-snake/blob/master/animation/snake.gif"
       alt="snake" />
</div>

## Steps:
    
1. Fork this repo
  
2. Generate a personal access token, to do that go to <ins>settings</ins> -> <ins>developer setting</ins> -> <ins>personal access token</ins> -> click <ins>generate new token</ins> -> select the `repo:staus` permission -> click <ins>generate token</ins>
  
3. Add the token to the forked repo's secrets, to do that go to the <ins>forked repo's settings</ins> -> <ins>secrets</ins> -> <ins>actions</ins> -> click <ins>new repository secret</ins> -> enter the name `ACCESS_TOKEN` -> and pase the token in the value field -> click <ins>add secret</ins>
  
4. To generate the first image without waiting for the secheduler, go to the <ins>forked repo</ins> -> <ins>actions</ins> -> click on the `Generate GIF` workflow -> click <ins>run workflow</ins>
