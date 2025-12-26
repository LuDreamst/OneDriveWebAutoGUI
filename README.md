# OneDriveWebAutoDownloader  
又一个没啥用的小玩意儿  
  
A simple and crude .py based on pyautogui to make downloading files separately from OneDriveWeb easier.  
## 1.背景/Background  
OneDrive网页端下载整个文件夹速度比较慢，连接中断可能造成严重损失；依次下载单个文件速度较快，而且较为可靠，但需要频繁点击。  
  
Downloading an entire folder via OneDrive Web is rather slow, and connection interruption may lead to severe losses. Downloading files one by one in sequence is faster and more reliable, yet it requires frequent manual clicks.
## 2.工作原理/Principle  
pyautogui截区屏幕画面，并识别、定位所需视觉要素；根据视觉元素的坐标，模拟鼠标移动即可代替手动点击，实现自动批量下载。 

Pyautogui captures regional screen frames, identifies and locates required visual elements. It simulates mouse movements according to the coordinates of these visual elements to replace manual clicks, thus achieving automatic batch downloading.
## 3.工作流程  
1.定位已有的checkMark样式，取消勾选并勾选列表中的下一个checkMark（整个过程中最多同时出现一个checkMark）;  
2.点击下载按钮（downloadButton）；  
3.等待若干秒至可能的downloadDone消失，再次出现downloadDone时循环这个流程。

1.Locate the existing CheckMark, uncheck it and then check the next CheckMark in the list (only one CheckMark shall be selected at any time during the whole process);  
2.Click the downloadButton;  
3.Wait several seconds until the possible downloadDone prompt disappears, and repeat the above process when downloadDone appears again.
## 4.已知问题  
1.鼠标滑轮偏移量无法与界面完美契合，循环过程中checkMark位置会逐渐发生偏移（此过程可以很慢，大概几百次循环后），严重时无法识别到checkMark，程序抛出异常或重复下载同一文件。将测试，1920x1080分辨率，浏览器全屏＋默认缩放的情况下，偏移量为-59时，checkButton逐渐向上偏移；偏移量为-58时，checkMark逐渐向下偏移。  
2.下载进行至列表末尾时，模拟鼠标滑轮操作不会导致画面滚动，此时会重复下载同一文件。  
  
1.The mouse scroll offset fails to perfectly match the interface, causing the checkMark position to drift gradually during the loop (this drift can be very slow, usually after hundreds of loops). In severe cases, the checkMark cannot be recognized, leading to program exceptions or repeated downloads of the same file. Tests show that under the 1920×1080 resolution with browser full-screen mode and default zoom, a scroll offset of -59 will make the CheckMark drift upward gradually, while an offset of -58 will cause it to drift downward gradually.  
2.When the download process reaches the end of the list, simulating mouse scroll will not scroll the interface, resulting in repeated downloads of the same file.
## 5.TODO
Nothing to do. It's just a useless tiny design. It just works, generally.  
## 6.注意事项/Tips  
1.开始执行时，勿遮挡checkMark样式，如果没有，手动勾选一个；  
2.运行期间，在除等待下载完成之外的环节操控键鼠可能导致错误；  
3.推荐将Web界面展开至全屏。  

1.Do not block checkMark when the script starts running; if no checkMarks, just mark one.    
2.During operation, manipulating the mouse and keyboard in any phase other than waiting for download completion may cause errors;  
3.It is recommended to expand the web interface to full screen.

