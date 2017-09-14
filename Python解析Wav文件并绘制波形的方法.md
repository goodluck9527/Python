# Python解析Wav文件并绘制波形的方法

> 本笔记来源于博文[Python解析Wav文件并绘制波形的方法](http://www.cnblogs.com/lzxwalex/p/6922099.html)

## Wav文件格式
* [Wikipedia上对Wav文件格式的解释](https://zh.wikipedia.org/wiki/WAV%20wikipedia%E4%B8%8A%E5%AF%B9Wav%E6%A0%BC%E5%BC%8F%E7%9A%84%E8%A7%A3%E9%87%8A)
  * **Waveform Audio File Format（WAVE，又或者是因为扩展名而被大众所知的WAV）**，是微软与IBM公司所开发在个人电脑存储音频流的编码格式，在Windows平台的应用软件受到广泛的支持，地位上类似于麦金塔电脑里的AIFF。[2] 此格式属于 **资源交换档案格式(RIFF) **的应用之一，通常会将采用脉冲编码调制的音频资存储在区块中。也是其音乐发烧友中常用的指定规格之一。由于此音频格式未经过压缩，所以在音质方面不会出现失真的情况，但档案的体积因而在众多音频格式中较为大。
## RIFF格式
* [Wikipedia上对RIFF格式的解释](https://zh.wikipedia.org/wiki/%E8%B3%87%E6%BA%90%E4%BA%A4%E6%8F%9B%E6%AA%94%E6%A1%88%E6%A0%BC%E5%BC%8F)
  * **Resource Interchange File Format（简称RIFF）**，资源交换文件格式，是一种按照标记区块存储数据（tagged chunks）的通用文件存储格式，多用于存储音频、视频等多媒体数据.Microsoft在windows下的AVI、ANI 、WAV等都是基于RIFF实现的.
