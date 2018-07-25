#### NOTE:

1. 
   > 实际上不管是在Django开发服务器上，还是在nginx+uwsgi+django部署的服务器上，都可以直接通过url访问静态文件，不需要在Django中专门为每个静态文件编写url路由和视图。比如，通过http://www.liujiangblog.com/static/images/default_avatar_male_50.gif你就可以直接获得网站用户的默认头像图片了。

----
      

2. > 很显然，{% static %}模板标签不能用在静态文件，比如样式表中，因为他们不是由Django生成的。 你应该使用相对路径来相互链接静态文件，因为这样你可以改变STATIC_URL （ static模板标签用它来生成URLs）而不用同时修改一大堆静态文件中路径相关的部分。