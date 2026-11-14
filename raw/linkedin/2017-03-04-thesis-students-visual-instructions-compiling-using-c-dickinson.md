---
title: "For Thesis Students: Visual INSTRUCTIONS FOR COMPILING the SWMM5.DLL USING MICROSOFT VISUAL C++ 2010/2012"
kind: linkedin-article
author: Robert Dickinson
url: https://www.linkedin.com/pulse/thesis-students-visual-instructions-compiling-using-c-dickinson
created: "2017-03-04 19:34"
published: "2017-03-04 19:40"
words: 517
export_sha256: a13a72144a43698396ef1150239d25ccb2c96ed65316d7811bb70bdf8467f738
---
# For Thesis Students: Visual INSTRUCTIONS FOR COMPILING the SWMM5.DLL USING MICROSOFT VISUAL C++ 2010/2012

For Thesis Students: Visual INSTRUCTIONS FOR COMPILING SWMM5.DLL USING MICROSOFT VISUAL C++ 2010/2012

========================

> **The following is based on the readme.txt for compiling that EPA distributes with the SWMM5 install**

1\. Open the file swmm5.c in a text editor and make sure that the

compiler directives at the top of the file read as follows:

//\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

// Leave only one of the following 3 lines un-commented,

// depending on the choice of compilation target

//\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

//#define CLE  /\* Compile as a command line executable \*/

//#define SOL  /\* Compile as a shared object library \*/

\#define DLL  /\* Compile as a Windows DLL \*/

2\. Create a sub-directory named VC2010_DLL under the directory where

the SWMM 5 Engine source code files are stored and copy SWMM5.DEF

and VC2010-DLL.VCPROJ to it.

3\. Launch Visual C++ 2010 and use the File / Open command to open

the VC2010-DLL.VCPROJ file.

4\. Issue the Build Configuration Manager command and select the

Debug configuration.

5\. Issue the Build VC2010-DLL command to build SWMM5.DLL

(which will appear in the Debug subdirectory underneath the

VC2010-DLL directory).

NOTE: The VC-2010 project file includes Open MP support which is

only available in the Professional and higher versions of

the compiler.

![](https://media.licdn.com/dms/image/v2/C5112AQFtwDRoNJxksQ/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1520242425793?e=1795651200&v=beta&t=tbGVpvBRIVlX2PPa8TQeAOMd4qPhyRTZktrhdLnLcuQ)

A SmartArt view of the process

![](https://media.licdn.com/dms/image/v2/C5112AQGGAu1k63HBbw/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1520141550003?e=1795651200&v=beta&t=nX2iYf_VOl-YhRDVfOvu4wnrisEQHzjXvgwvs1OO94o)

How it looks in the Windows directory

C:\SWMMandSoftware\VisualStudioSWMM5\swmm51010_engine\VC2010_DLL

Arbitrary Windows directory name with a Subfolder of the SWMM 5 engine followed by a Subfolder called VC2010_DLL with files SWMM5.DEF

and VC2010-DLL.VCPROJ

How it looks in Visual Studio 2012

![](https://media.licdn.com/dms/image/v2/C5112AQE8kr-1SPJjfw/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1520146800750?e=1795651200&v=beta&t=4tpOign3IMRj9n4DI1YLy2beDJqp8eBtQAXh1-9VWbE)

And here is how it compiles right away

Generating Code…

Compiling…

shape.c

snow.c

stats.c

Generating Code…

Creating library C:\SWMMandSoftware\VisualStudioSWMM5\swmm51010_engine\VC2010_DLL\Debug\VC2010-DLL.lib and object C:\SWMMandSoftware\VisualStudioSWMM5\swmm51010_engine\VC2010_DLL\Debug\VC2010-DLL.exp

VC2010-DLL.vcxproj C:\SWMMandSoftware\VisualStudioSWMM5\swmm51010_engine\VC2010_DLL\Debug\VC2010-DLL.dll

========== Build: 1 succeeded, 0 failed, 0 up-to-date, 0 skipped ==========

If you want the Release version use Build/Release

![](https://media.licdn.com/dms/image/v2/C5112AQENCUzIy_V1cQ/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1520041132805?e=1795651200&v=beta&t=tD06CSiZVbAfiLC5AEhs8OIGg5ceoN8q04S9XE90xds)

Note on April 28, 2017 - I am including a link to a zip file of a working directory in VS 2012 and the directory C:\SWMMandSoftware\swmm51012_engine

You can download the entire directory (working using this link) [http://blog.innovyze.com/wp-content/uploads/2016/09/swmm51012_engine.zip](http://blog.innovyze.com/wp-content/uploads/2016/09/swmm51012_engine.zip)

> A Master File from SWMM3/4/5

[http://swmm5.org/2017/06/02/extran-hydraulics-master-from-extran3-and-swmm4-converted-to-swmmn5/](http://swmm5.org/2017/06/02/extran-hydraulics-master-from-extran3-and-swmm4-converted-to-swmmn5/)
