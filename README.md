# LantraDict
一个使用 Flask 框架制作的查字项目（数据来源于 Python 包 xy_zidian ）  
初学者写的第一个项目，有诸多不足之处敬请谅解并给予建议，谢谢。

> ### 开发环境
> - Python 3.10.5
> - macOS Monterey 12.5

## 使用
- 使用前需安装以下Python模块：xy_zidian, pypinyin, zhconv, flask。推荐版本（开发版本）见下：
> xy_zidian==1.0.0  
> pypinyin==0.46.0  
> zhconv==1.4.3  
> flask==2.1.3  

- 如果运行时出现错误可尝试更改端口：
~~~ Python
app.run(port=你的端口_YOUR_PORT, debug=True)
~~~

## 注意
该项目已提供 **纯 html+css+js** 版本，见：[LantraDict-js](https://github.com/JaxonMa/LantraDict-js)。
