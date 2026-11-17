---
title: "Water Talks: the ICM SIM engine and the ICM SWMM engine (webinar transcript)"
date: 2021-04-27
date_note: "Inferred, not stated: ICM 2021.3 and SWMM 5.1.015 are current, and three weekly sessions follow, the last on May 18. Open question Q96."
speakers: "Nathan (Innovyze systems engineer, host; surname not given) and Robert Dickinson"
series: Water Talks (Innovyze webinar series, on GoToWebinar)
link: https://lnkd.in/p/gX8v9RQB
supplied_by: Robert Dickinson, 16 November 2026, as a time-stamped transcript
---
# Water Talks: the ICM SIM engine and the ICM SWMM engine

About this file. Bob uploaded this time-stamped transcript in a Claude session on 16 November 2026 and gave the link above for the recording. The text is an automatic caption transcript: names and terms are often garbled (see the source page for the readings). Claude (Anthropic) removed only the page's "Read More" and "Show less" lines; every time stamp and every word of the transcript is as received. The webinar was run by Innovyze; Nathan's words are his.

00:04
All right, good morning. Good afternoon.  Welcome to Water Talks. Uh  So, today um we're going to be getting  into um uh a little bit more of the  engine uh numerical theory and some some  differences. So, um I think this is  going to be maybe a little bit more uh  academic than than some of our previous  Water Talks.
00:23
 So, hopefully um if that's  of interest to you, um this this will be  a good one. Uh this one's topic the  differences between the ICM SIM engine  and the ICM SWMM engine. Um so,  when we say ICM SWMM engine, that might  be confusing to you. So, for those that  that don't know, we added the EPA SWMM  engine as an option inside of ICM. Um  we'll we'll be talking about that, but  so essentially we're using ICM as a  platform for all these comparisons that  we're going to be talking about.
00:52
 But  really, we're using SWMM EPA SWMM  um as it is.  Um so, that's what we'll be getting  into. Um I know there's always a  continual attendees trickling in over  the first uh 2 minutes. So, I'm kind of  slowly stepping through, but soon what  we'll get into it. So, um the host today  uh so, I I'm Nathan. Um  I'm a systems engineer within Innovyze  I've been here 6 years.
01:19
 I used to be  doing support where I would help support  with ICM and ICM LIVE and InfoSWMM and  some of our uh as well as our water  modeling tools. And joining us is Bob  Dickinson who he's he's been in the  industry for a long time. Um in case you  don't know him, he has he has a blog and  he actually helped write the EPA SWMM 5  engine back back in the day, right right  Bob? Um do do you want to introduce  yourself?  Yeah, yeah, basically uh yeah, a long  long history of SWMM.
01:48
 SWMM 3, SWMM 4, XP  SWMM uh SWMM 5 from 2001 to 2006.  Been at Innovyze since the end of 2007.  And um  I I really love um what we've done with  um  the SWMM networks inside of ICM. So,  what we're going to talk about here is  um Saint-Venant differences, numerical  differences, but we'll show you how you  compare SWMM 5 engines to ICM SWMM  engine results using the ICM GUI.
02:21
 So, thank you. Thanks for attending.  Yeah, great.  So, um So, as as always, uh this we we  we kind of aim to make these water talks  a little bit more informal. You know,  you probably didn't come just for a  polished presentation, but we want to um  open up the questions panel. So, in your  GoToWebinar, um if you're new to this,  um you can enter your own questions  here.
02:43
 Um and with Bob and his long  history of the SWMM engine, as well as  working alongside our ICM engine, this  is a great chance to ask ask your um  nitty-gritty uh  you know, questions that you might have  on you know, why are things a little bit  different. So, if there's anything he  mentions um in passing, you know, feel  free to to jump on with a question.
03:04
 We'll see those and we'll try to um  address them as they come in um or or as  it as it fits in. So,  please uh share your questions. That's  what makes this fun.  Um and some upcoming water talks. Uh  we we've we've updated the site, so now  we have um three more upcoming topics.  Uh so, next week,  um one thing I'm kind of excited for is  we're going to share tips and tricks for  real-time controls in ICM.
03:32
 So,  um we're going to be bringing Nikki, um  Nicole uh Hawthorne, who has been  supporting our ICM user base in North  America for 11 years, I want to say. And  so, she's come across many um pitfalls  that users commonly make with setting up  real-time controls because  RTC, let's face it, it's not something  we set up on a daily basis and it's  really easy to forget the details, but  ICM is very powerful and comprehensive,  so we're going to cover that.
03:57
 Um  then the following week  I'm going to join our project manager of  Info360.  So Info360  can integrate with your SCADA data and  tie into  hydraulic modeling like with InfoWater  Pro or WS Pro.  Eventually we're also going to to to do  it with sewer and storm modeling. Um so  we're going to talk through the process  of getting your data ready for Info360  and what that implementation looks like  and how you can start preparing today  for kind of this digital transformation  of of taking your model that next step  to connect it with SCADA.  Um  and then finally May 18th  kind of a a session on ICM basics. So  we're going to kind of talk through talk  through some basic things. So  definitely admit that this these four  sessions are a little bit more InfoWorks  ICM heavy. I know we have some other
04:56
 asset management drainage design and  some other topics coming up after this,  but that's the lineup, so head over to  the website if you're interested to to  register for any of those.  Um and with that I am going to hand it  over to Bob to start off with some  slides. Bob, I'm going to make you the  presenter.  Thank you, Nathan.
05:16
 And  yeah, Bob's going to present a few  things and we'll we'll kind of go from  there.  See my screen yet? Yep, I see it.  Okay.  Right.  Okay, there we go.  All right, so  to start out  what we're going to be talking about is  ICM SWMM networks inside of the ICM GUI.  So you basically have um, an ICM  network, so if you click over here, you  see this ICM network.
05:51
 This is um, a SWMM 5 network. So, we use  the same engine as  SWMM 5. What's nice about it is that we  have a lot of import from uh, InfoSWMM,  XP SWMM, SWMM 5, and it brings in  what's been a common complaint in the  past, we'll bring in the in the in the  uh, rainfall data, the pattern data,  etc.
06:11
 So, you no longer have to like do a  lot of copying and pasting of getting  data together.  But, before we do this comparison, we  want to go into what is inside of the  model.  So, we're going to look at the screen.  So, slideshow.  So, as I mentioned, um,  what we're able to do is, for example,  this the  the uh, the model that I'm showing you  today, I have about a hundred um,  models of SWMM 5  imported from SWMM 5 or InfoSWMM or XP  SWMM into ICM SWMM networks, and then I  converted them using the ICM GUI into  um,  into ICM, and I can do a direct  comparison. However, when you do the  direct comparison, you can see model  differences. So, I wanted to go over  what the differences are between the ICM  SWMM engine, which is known as the  Wallingford ICM model, and the SWMM 5
07:09
 engine inside of um,  inside of ICM SWMM networks.  Uh, but yeah, before you go on, um, I I  just find it very interesting. You've  got a pretty impressive database of  different models that that you've  brought in. You mentioned a hundred  different models. Um, I I think you've  mentioned at one point, don't you have  like automated testing? So, as we've  been bringing the SWMM engine into ICM,  we've been doing like nightly builds and  testing of the engine, right?  Yeah, uh, you're getting a little bit  ahead, but we have this thing called  called the One SWMM engine, and it's our  engine that we use for the ICM SWMM.  It's It's It's also used extensively  inside of InfoSWMM and InfoDrainage and  we have at least 500 test files that we  run EPA SWMM. The current EPA SWMM is 5.  5.1.015  and the OneSwim engine and we do  basically statistical comparisons of all  the nodes and and links so that
08:09
 we're we're we're happy that there's  been no regressions or no changes in our  code that give a different answer than  than InfoSWMM than than  SWMM 5. So, those are done every night.  In fact, I accidentally turned on my  notifications so every night I my watch  tells me three or four times that you  have a new engine.
08:28
 Uh so, need to figure out how to turn  that off.  Um  500. So, out of these 500 I I imported  about 100 different um  ones that I've that I've used in the  past. A lot of these are familiar to you  who  who did the SWMM or or used SWMM 5 and  also  used the OWA um  website GitHub site um because those are  a lot of testing files.
08:50
 So, anyway,  that's a general idea.  We have 100 models both in ICM and both  in SWMM and OneSwim which is tested to  make sure we have the same answers as  SWMM 5.  Um as I mentioned um  what's nice about ICM SWMM networks is  you get all of the bells and whistles of  ICM.  So, you can get the same exact HDL  graphs, you get the same import export  through CSV files, through shape files.
09:21
 And in the current version, actually  have a a future version. In the current  version 2021.3,  we actually have um ICM SWMM 2D  ability. So, it uses essentially the  same 2D engine that ICM does. So,  everything's sort of merging together,  you know,  nice nice little interface. So, all the  tools  are or are usable in in both ICM SWMM  and ICM.
09:48
 However, and this is very  important, they use different Saint  Venant or 1D engines.  So,  just to go a little bit of history here,  um  we're we're looking at SWMM 5 either All  these models started out as SWMM 5. As  everybody knows, we've been five  different um  SWMM 5s. Current version is 5.1.015.  And soon uh EPA will release 5.2 based  on what Lou Rossman  mentioned at uh the CHI conference in  February.
10:22
 In addition, um  this GUI also has InfoWorks ICM, which  has a really long history going back at  least to the late '70s.  Um where it was uh Wallrus, uh SPIDA,  HydroWorks CS,  uh a few RS versions, and then currently  ICM I guess since 2009. And ICM actually  has a lot of SWMM 5 components. It has  SWMM 5 water quality, uh SWMM 5 LID's,  though it's called SUDs in  in ICM. Same same thing.
10:53
 It has SWMM 5 RDII. It has SWMM 4 RDII  actually. And it also has SWMM um  hydrology  and SWMM infiltration. So, Green Ampt  and the modified Horton inside of ICM is  actually SWMM. SWMM 5 or SWMM 4. Then we  have XP SWMM, which is SWMM 4. InfoSWMM,  which uses SWMM 5. And then as many of  you probably know, we were recently  acquired by Autodesk.
11:20
 And Autodesk as  actually has  something called Autodesk SSA, which is  really kind of a cool  um program that sits on top of InfoWorks  um  It it sits on top of um AutoCAD Civil 3D  and runs a a modified SWMM 5 engine with  um  with some BOSS engineering um  HEC-RAS capability.  In addition, we also have InfoDrainage,  which is our um  design software for  uh small drainage areas.
11:50
 It uses a a lot  of LID's and SUDS. And that the little  the guys the stars basically means it  uses a shared engine. So, that's the one  SWMM engine. That's the one we test  every night.  And then the InfoWorks ICM network uses  also the one SWMM engine. So,  a lot of SWMM stuff and we're trying to  make  basically one SWMM work really well  import and output output and make it  look as nice as ICM.
12:17
 And so, to that to  that extent, we have a lot of  import facilities for XP SWMM, for  InfoSWMM,  all the different SWMM 5 um features. We  even have an import for InfoDrainage.  So, a lot of SWMM things and um  now we go on to uh the Saint the shallow  water equations or the 1D Saint-Venant  equations.  Um this is something I just took out of  Wikipedia.
12:49
 Basically, you're solving for the  conveyance,  the depth, and the flow inside of um  inside of a 1D channel. And the 1D  channel could be a pipe, it can be an  open open length.  Uh it could be trapezoid, it could be a  like a HEC-RAS section, etc. And to get  that, the main the main features are  what the cross-sectional area is,  the hydraulic radius, and the wetted  perimeter.
13:15
 So,  those are common to all Saint-Venant  equation solutions.  And if you look down here, what we're  going to look at is the differences  between the ICM SWMM  and the ICM SWIMM SWIMM engine.  So, here we go.  There's actually three solutions inside  of ICM. You have ICM conduit, you have  ICM pressure, and ICM force main.
13:43
 And they use different parts of the  Saint-Venant equation. So, for example,  the conduit has a continuity equation,  it has the unsteady flow term,  non-linear term, it has the water  surface slope, the bed slope bed slope,  and the uh  and the conveyance term. The conveyance  term basically is a friction loss term.
14:02
 Um in in ICM  you have the option of using Manning's  or Colebrook-White. And that's where the  K comes in. So, it's similar to SWMM 5,  but it has two options.  Also, a a a lot a little known feature,  if you use force mains in ICM and use a  Hazen-Williams,  it converts it to Manning's equation  using the SWMM 5 equation.
14:23
 So, you're  still using Colebrook-White or or  Manning's, but it uses that. Now,  when ICM switches to pressure you tell  ICM to use pressure or  um  force main, it it it it basically drops  out  the partial A partial T term, still does  this term, drops out the non-linear  term,  and it still does the bed slope and the  water surface slope, and it still does  the uh  the the uh conveyance term.
14:53
 Now, if you  look at ICM SWMM or SWMM 5,  it also has the same continuity  equation, it still does the unsteady  term, non-linear term,  um instead of doing um the water surface  slope, it does the head, and the head  basically is the water surface slope  minus the bed slope. And it does the  friction loss, and the friction loss is  Manning's equation for partial flow,  Manning's equation for pressure flow if  you're not using the force main option.
15:26
 And if you're using a force main option,  it uses Hazen-Williams or Darcy  Darcy-Weisbach equation. There's a  slight difference there.  And just like ICM, when you're when the  when the pipe becomes full,  you drop out the non-linear term.  Also, if you're familiar with SWMM 5,  there's a few options called keep,  dampen, and ignore.
15:47
 That basically gives you options for  how to drop this out or not.  Now, we come down to a really  significant difference between ICM and  SWMM for  losses.  SWMM 5 does not have losses at the  nodes. It has losses in the links.  So, this GA  HL basically is entrance excess and  other loss, or in other words, KV  squared over 2G.
16:10
 ICM is totally  different. ICM actually does not use a  node continuity equation.  It calculates the head loss based on  five different options. And that head  loss then interacts with the um  upstream or downstream depth in the in  the link. So, there's a better  integrated head loss equation inside of  ICM versus just doing it inside the  link.
16:36
 So,  um a lot of equations here. The main  thing is that there's a lot of  similarities because of the same same  finite solution between how it does  partial flow  and how it does force main flow or  pressure flow.  And the similarity is dropping out the  non-linear term, etc.  Okay. Now, we come to another really,  really big difference between ICM and  SWMM 5.
17:00
 SWMM 5 only has  one flow in a link.  So, it calculates the flow in the  midpoint based on the upstream area and  the downstream area,  hydraulic radius upstream and  downstream, and the width upstream and  downstream.  And that is kind of a big source of  instability in in SWMM 5 because what  happens is a lot of times you have flow  and oscillating from one end to the  other.
17:23
 Now, in ICM, there's at least five  points along a link  where it uses the pre-spin um  pre-spin um implicits um  scheme. So, it it's a lot smoother as it  goes in and out of a node because it has  more data points. And the user can  actually um increase this or it could be  done automatically by the program. So,  one of the big reasons ICM tends to be  smoother, not only is it implicit, it  has more computational data points.
17:53
 Now,  you can do the same thing in in SWMM 5.  For example, Auburn University and and  their colleagues in Brazil  have a have a um  an add-on or an app for SWMM 5 that will  basically break SWMM 5 node up into  smaller parts so that  you basically can have  as many um links as as you need to make  make that stable and and do the slot  slot more.
18:19
 So,  more data points to look for ICM and a  better integration between the node and  the node and the links  um often makes for a more stable model.  Okay.  Now,  as I mentioned um SWMM 5 is a link node  model. So, essentially, the node area  is used and the node area is the node  area plus  the area of the links, etc.
18:47
 So, that's a  totally different method than than than  ICM.  But, you calculate it based on the flow  into the node and the um  area of the node.  Now,  um the ICM uses six head loss of types.  It has nor has none, normal high, fixed,  user defined, and FHWAA. Fixed is the  same  values that you would use in SWMM 5. So,  you get for example, you have an exit  loss.
19:15
 So, one all your velocity head is  lost. But, the big difference is that  because it's using a  uh matrix solution, the the head loss  here is integrated with the depth here  and the depth here so that you get a  smooth um  transition. So.  Here we go. And if you need to know more  about that, there's a very good head  loss technical technical note in the ICM  help file.
19:42
 Hey Bob, before you leave that slide, um  so there there was an interesting point  you made on uh SWMM has one  computational point on each pipe and and  ICM has has five or more. Um cuz cuz  you've you've uh been in many support  cases where SWMM models become unstable,  right? If they have like some some  models will have really long force main  pipes, and that that's a common problem  to watch out for.
20:06
 Yeah, in in that case, um kind of like  what Auburn University does, you can add  a break node. Basically, break for  example, say you had a 5,000-ft long  force main. Break that force main up  into three or four parts by sticking in  intermediate nodes.  And with a high surcharge  head.  Um so so basically, you you you make it  a little bit  little bit more like ICM and a little  bit more um  little bit more um  more more um segments inside of the  original link.
20:38
 So, yeah, that's that's a  good point to mention.  Yeah, and on long pipes, ICM is kind of  dynamic in how it inserts those those  computational points, right? It's kind  of a relative to the length and the  diameter.  But, a minimum. Yeah. Okay.  Yeah, there's like a minimum step and a  a minimum space step and a maximum space  step.  Okay.  Now, slot.
21:00
 For a long time, SWMM 5 did  not have a slot, and Lou Rossman added  that in  uh a a version of of SWMM 5 2 years ago.  So, in I in uh, SWMM 5 you have the  option of using XTRAN or slot. I really  like the slot because the slot basically  allows basically for smoother  transition. So, instead of switching  from  um, the Saint-Venant to a to a point  duration for surcharge flow, it uses the  a concept of a slot and allows the the  same equation to be used all the time.
21:35
 And same thing happens in ICM. If you  have a slot in the conduit, you um,  basically  have a um,  basically a a uniform or a smooth  transition from free surface flow to  partial flow.  Now,  what's a little bit odd and and  different is so, in a SWMM 5 force main,  it's still using the slot. In ICM, if  you use a force main, it does not use  the slot and it basically drops out a  few few other terms.
22:01
 So,  uh, that that that's a little little  odd, but basically, the idea of a force  main in ICM is to make it basically run  full all the time.  Um, in addition, ICM has some really  neat um,  mode switching. So, for example, if you  um,  if it if it needs to use pressure, it  will switch to pressure back and forth  and and you'll see that in the in the  log.
22:26
 So, ICM has a lot of built-in, I  don't want to call it machine learning,  but a little a little  a lot of 40 years of experience of of  testing models and getting models to  work. So, there's a lot of little  options you can do in in ICM.  So, the slot, if you do a comparison  between SWMM 5 and ICM, it's a good idea  to use the slot option in SWMM in SWMM  5. That matches better what ICM does.
22:52
 Um,  in SWMM 5 and um, I mentioned Auburn  University. Auburn University has  versions of SWMM 5 where they change the  slot width. In SWMM 5, the slot width is  1%.  Um when it when it's full when it's um  not full is basically at the peak, it  uses so sure  formula. In ICM, you have a little bit  more control.  It has something called the celerity  ratio.
23:14
 So, depending on what the  celerity ratio is, you can have  1%, 2%, or  any kind of percent of um  uh slot width. So, that  makes it a little bit um easier. So, the  user has a lot of control in ICM over  a lot of different parameters. For  example, the slot width.  I'll give you an example here. So, 14.4  is is 1%. 20 would be um 2%.  All right.
23:44
 Now, we get into sort of the  magic of ICM.  What ICM does is um  it essentially allows you to  sort of what Nathan was saying of  issue issue of long force mains. If it  it has a default of five. If you have a  very long force main or a very long  pipe, it'll actually make further  divisions so that for example, there's  there's not a maximum time maximum it  doesn't exceed the maximum space step or  the minimum space step.
24:13
 So, if it needs  50  uh computational nodes on a long length,  it will it will use that.  You can also have direct comparison or  direct uh slot widths. So, you can enter  that there or you can use the celerity  ratio. There's a lot of different ways  of doing that.  Uh this is another common feature  between SWMM and SWMM 5 and ICM.  Uh there's characteristic Froude numbers  where basically it starts dropping out  the non-linear term based on the Froude  number.
24:43
 Okay. Now,  one one another big difference is that  in ICM, you give it a time step. So, for  example, 60 seconds. It'll calculate the  time step needed  for the whole system to basically  iterate and converge. If it doesn't do  that, then it does a time step having  and it does the and it tells you what it  does in log in the log file.
25:07
 Um in SWMM 5, you give it a time step  and then it'll based on the um  CFL time step criteria, it'll figure out  what the time step it should be using.  However, it doesn't do the time step  having.  So, it never never goes below  uh whatever it figures out for the CFL.  Now, in our other software, XP SWMM, it  actually does the time step having.
25:29
 So,  that's  a slight difference between XP SWMM and  SWMM 5. It does the slight time step  having.  All right, and it's pretty pretty  powerful here.  Um in addition,  you also have a  other features. For example, in the  simulation  for ICM, you can turn off um  the drop inertia term, so that basically  makes it more act more like a diffusion  wave  equation.
26:00
 Okay, another really good thing is um  ICM has a job progress window. So, it'll  tell you what time step it's using  currently,  how many times it's failed, what the the  the link that's failed or the node that  failed. So, if you have a big model, you  can get some feedback from the model  about what basically kind of geometry  issues you have or perhaps too much  flow,  maybe a bad river reach or bad 2D  connection, etc.
26:28
 And what's similar is that we have the  same  same look to the to the software.  Okay.  Another when you're trying to do these  graphics, another big issue is that I  mentioned SWMM 5 only has one flow in  the middle of the link.  ICM has five or more. However, the  graphics only show the upstream and  downstream.  So, when you're doing a graphical  comparison, just remember  I'm picking either upstream or  downstream in ICM and I'm comparing it  to the midpoint in SWMM 5.
27:03
 All right, so that's quite a quite a  difference. But, all other than that,  the graphics are the same.  The look and feel of the graphics are  exactly the same. The geo plans are the  same, etc. for ICM SWMM and the ICM SWMM  network.  Um a little node feature a lot of times,  oh, how do I find where the where the  hydraulic jump is? You can actually add  point results in ICM.
27:29
 So, for example, I can break this up  into five points, then I can graph the  points there. So,  you can have um  further discretization  graphically, but you have to tell it and  give it the points per line  of what you want to see. But, normally  it just shows upstream and downstream.  Um I mentioned um  the log file.
27:50
 In ICM, there's a log file  which tells you  what what it what um what time step it's  using, history of time steps, when it  switch back and forth,  uh what happened when it didn't why did  it have to I lower the time step and  what time step did it go back to.  Um in SWMM 5, we have something similar,  um but basically  you would normally see that you have to  use a lot smaller time step in SWMM 5  than you do in  do in ICM.
28:17
 And then also gives a time  step frequencies here. So,  log files and report files are are key  here. Hey hey Bob, can you can you step  back there? Um yeah, I I feel like these  are these are common time steps that I  see where in SWMM, you know, I might  have to be going, you know, less than a  second for the time step cuz it's using  that CFL number.
28:35
 And then in ICM, um  you can see that it's actually taking a  60-second time step, which in the SWMM 5  modeling world, I feel like that's it's  of absurd that the model is taking a  60-second time step. Uh and it does  that, you know, cuts it down as needed.  But, um can you can you mention why ICM  is able to take such a larger time step  than SWMM for like the same model?  It's a It's a Okay.
29:00
 SWMM is a Picard  successive successive um iteration. So,  basically,  it'll it solves each node and each link  separately  and then iterates and the iterations  normally four to eight um iterations  until it until it converges.  Um in ICM, it does a matrix solution  using the free SWMM um  uh four-point box.  And so, essentially, it could because it  uses  as further discretization and it uses an  implicit solution, it can use this small  time step. Here's a good example.
29:33
 I'm  going to show you the results later for  this, but if this is the um siphon  example, in ICM, it had to go down to  7.5 seconds as it was filling up the  siphon.  In SWMM 5, it had to go basically 1  second and then we're kind of like stuck  at 1 second  um the rest of the simulation because in  SWMM 5, it you basically have to pick a  time step that  is the worst is the time step for the  worst case  uh situation during your  during your simulation.
30:05
 Whereas in  in ICM, it figures out, "Hey, I have a  really big problem here. I'm going to  lower the time step." But, once that  that's that's done, it then goes back to  the to the original time step. So,  that's another big reason that ICM would  be faster  uh because it can go back to the  original time step.  All right.  Thanks.
30:28
 Um and then in SWMM um in ICM also, if  you have a problem, you look at the log  file, it'll tell you what what node or  whatever was non-converging. So, this is  means that during the top time steps it  was not converging.  Um um for that. So, that  sort of hit or miss, but you can get  some information about your model from  that.
30:52
 Um and this is from Nathan. One one of  the issues kind of weird issue um  when you I So, the way I made these  models I imported SWMM 5 or InfoSWMM or  XP SWMM into ICM SWMM.  And then I converted it to ICM. However,  when you do that ICM likes to rename all  of the uh  pipe links. So, when they try to do a  graphical comparison it doesn't work  because ICM has a different name than  than than um the ICM SWMM.
31:17
 So,  came up with this. Basically, whoops.  Basically, you reset the you just do a  SQL set.  So, that you just  convert um the the the the link names in  I and ICM SWMM to ICM. Then everything's  works out perfectly. And then I save it  in user text  as the original. So,  that's not good.  All right. Now, let's go to um  this.
31:50
 So,  I'll show the worst first.  So, the way we made this is imported  SWMM 5  siphon model.  Uh ran it and then did that set  set example and then converted it to  ICM.  And then we did the graphics and then I  did making a flow surface. So, what I  what I did was I exported all of the uh  um ICM SWMM results to a  to a CSV file then imported back as a  flow surface.
32:27
 So, then you can make a  custom graph and then you can look at  the uh  graph. Okay.  I have a little bit of problem with the  data points, but basically you can see  what happens. SWMM 5, that's SWMM 5  here,  had some issues in the beginning and  then it basically matches ICM the rest  of the way,  but because SWMM 5 is less flexible with  the time step, you were stuck  using a 1-second time step or 2-second  time step the whole simulation  there.
32:55
 Whereas I Whereas in ICM you uh  basically kept on going.  Some more uh examples.  So you can see especially the velocity  can quite  quite different, but flows basically  basically match, so  um you can look at look at that.  And let's close that window.  So um So Bob, yeah, just to just we can  understand what what those graphs are.
33:33
 Um so you you were doing like a inverted  siphon model?  Um  I'm doing an inverted siphon model. So  let's look at the siphon.  Yeah.  Let's fast forward here.  Yeah, so  comparing ICM and ICM SWMM for this  inverted siphon model,  um so essentially  uh SWMM was having a little bit of a  problem in the beginning and um it  actually worked better with the slot  than than than the XTRAN solution, but  um  it allows you to basically  uh  compare the two.
34:26
 So  that's  that's what we're doing here.  And you can also do things for example,  if I wanted to look at the  Look at this and I can look at the  results.  And let's look at the  link  node and depth.  So this is the ICM SWMM. You can see  this is a little unstable in the  beginning. There's no continuity error.  You can check the continuity error just  like you do in SWMM 5.
35:06
 You  basically right mouse click mouse right  mouse click open as report file.  And at the top it's essentially a SWMM 5  report, but it tells you a little bit  more information. For example, um  what computer I'm using um  um and what my license is. I guess I  shouldn't show you that.  As well as the SWMM version, which is  for SWMM modelers out there.
35:31
 Yeah, so  you there's no continuity error,  but it becomes a little little unstable  in the beginning. Now, we can also look  at the ICM results.  So this is same model.  Here's our ICM result with our oops.  So let's select all elements and then  we'll do the same thing.  So what's what's cool is that you  basically look looks exactly like SWMM.
36:05
 I mean ICM SWMM looks exactly like ICM.  So here's the big difference here. I can  either look at the upstream or  downstream. It's hard unless you do the  intermediate points to to show that.  So let's look at ICM and you can see  there's a little bit of instability  there, but basically it's a lot smoother  than SWMM 5 and it shifts to 60 seconds  once it gets  over this point here.
36:29
 All right?  And um th- those were some really pretty  big pipes and you were starting it off  dry. Was that? Cuz I know that could be  a big difference between SWMM and ICM.  That's kind of interesting, isn't it?  Yeah. Now,  in um  run manager here,  um you could have you can actually  essentially I can drag  this simulation.
36:55
 So, it works just like  ICM. So, basically that's my hot start  file. Those of you familiar with SWMM 5,  you know about a hot start file. Well,  it's just like an ICM, you can give it a  a an initial initial state  or save the state. So, that's like  us- using a hot start file and making a  new hot start file. And that probably  would make the  the model run a little bit um a little  bit smoother in the beginning, except  for force main if I mean for a siphon if  you  you start out full, it's kind of defeats  the  the purpose there.
37:29
 Okay.  Uh parameters  over here under options is where you  basically give the process  the the surcharge method.  Time step is here.  Give it a time step.  3D parameters are here.  So, you give it the 2D parameters if you  had a mesh  etc. But, everything else basically  looks like uh  SWMM 5.  And another kind of neat thing is um  depending on what you're looking at.
37:57
 So,  for example, here  I'm looking at a um  You know, looks like I lost it. I'm  looking at a uh  ICM SWMM network. And by the way, that  shows up over here.  So, that says SWMM network, that says  ICM network.  I go to model, model parameters,  options.  Basically, it shows you what the swim  swim options are.  Now, if I was to go to ICM  and go to model  I get totally different parameters.
38:37
 So,  it's cognizant of what what engine  you're using during particular uh  particular simulation.  Okay, I kind of messed this up here. So,  what what is this happens, what you do  is  All right. That was that.  Go to window, make a new explorer  window.  Here we go.  Um you can do the same thing for other  models.  So, here's our classic user one from the  swim Q&A report.
39:21
 Run run that.  And do a graph.  You can see here which  is a little bit a little bit closer, so  uh  except for the depth in that one, but  you can see you can  better do a better comparison. And you  see sometimes there's a really close  comparison and sometimes it  it goes further apart.  Now,  here's our run. The run is the same.
39:56
 So,  for a long time when you import a SWMM 5  to ICM, you lost the rainfall data, you  lost the patterns.  What's nice about this is you import a  SWMM 5 file into ICM SWMM networks,  it makes a um  it makes a rainfall file and that  rainfall event, that inflow event, any  of these specialized features can be  used either in the ICM network or the  ICM SWMM network.
40:23
 So, it makes it really  easy to to  basically go back and forth between ICM  and ICM SWMM. You're using the same  rainfall data,  the same climate climatology, the same  uh SWMM patterns, etc.  And it also has um  the same ability, the same network. So,  if you want to do scenarios, you just go  over to your scenarios,  uh create a new scenario.
40:56
 So, everything works as basically the  same as  as ICM except the engine is different  and then depending on the context, you  you essentially um  um you essentially change  change the uh dialogues, etc.  Yeah.  Hey Bob, one one question that came in,  um I I see we have a lot of consultants  in the the audience.
41:20
 Those are usually  the ones that are have more appetite for  technical things like this. One question  that came up is, can you elaborate a  little on the easiest way to convert an  existing ICM model to a SWMM network?  Sure. So, yeah, I know even from this  network you can do network import from  InfoWorks.
41:39
 Uh yeah, I'll I'll let you  show.  I know there's a a number of different  approaches.  Yeah. So, for example,  here's our um  Here's our ICM network.  For For an ICM network, you can import  it from  InfoDrainage, MicroDrainage, RAFTS, um  SWMM 4, SWMM 5. You already You already  know knew those, so.  You can also import it from a SWMM  network, which is the ICM SWMM network,  or from XPX.
42:12
 So, if you come over here, I would then  just drag in  my um  my SWMM network  and then I can do that conversion.  Now,  um  so if you want to go from um  Let's go to  new SWMM network.  And we go to network, go to import.  And click here.  Yep, and then you can zoom to network.  Oh.  Yeah, I have to zoom all the time. There  we go.
43:01
 And then I do a validation.  And then I commit it. So,  very really really really really simple.  Okay, another really neat trick here is,  not really trick, but a neat feature, I  should say feature.  Um so for example,  here,  so here's one with hydrology.  So I click on  What did I do here? I clicked the wrong  one.  Clicked on the output.
43:37
 So I ran this model ICM.  I can right mouse click here  and export it to SWMM 5.  So let me go to my desktop.  Now I can come over here to a SWMM 5.  What's good about this is it brings in  the time series.  So, the time series basically  you come in live, so you you you no  longer have the issue, which is which  was sort of a pain, of having to copy  and paste rainfall and the patterns.
44:29
 Um  so, everything comes in smoothly back  into SWMM 5. So, we're really focused in  focused on SWMM 5 um import export uh um  ICM SWMM to ICM networks, ICM  um networks ICM SWMM networks, all of  our other products, for example, Info  Drainage or XP SWMM, Info SWMM can be  imported into this into this package.  Or into this into this uh GUI.
45:02
 All right.  Other questions?  Yeah, yeah, a question. Um does the ICM  run log include a summary of how the run  went? Is there anything like a  continuity error included in the ICM  log?  Uh  obviously ICM user there.  You do get  a PRN file.  And if you add up all of these, it's not  it's not as nice as SWMM 5, but it tells  you what the total rainfall volume was,  the total runoff,  total inflow, and the total outflow, and  how much was lost.
45:44
 And then over here, it sort of has um  some  some tables to tell you where the flood  loss was, etc. So,  I've seen clients, for example, San  Francisco had a really nice thing they  would  in some kind of macro, they would take  this in Excel and come up with a SWMM 5  like um  mass balance, but um  it's basically what you get.
46:08
 Oh, another um  I'll go ahead.  Oh, sorry. Um  another little hidden feature a lot of  people don't know about is um  Maximize this. ICM has some very good  diagnostics. Let me find it.  Yeah, can you maximize this window?  There we go.  Diagnostics. Turn on the time step log,  log RTC rule changes, log mode switches,  and output state.
46:43
 Then you'll get a lot  of data about what the actual time step  was, what rule is being used, and also  if it was switching from force main to  pressure mode. But you got to turn that  on, and also, you can have warning fresh  thresholds here for water quality or  volume balance, so you get a general  idea of what's what's going on.
47:01
 All  right. Uh  so, what was the next question?  Um yeah, I was going to say uh the the  log um the log file does include mass  balance continuity error with the 2D  engine, um as well as like 1D 2D uh  integration. But yeah, in general, I  find that 1D models in ICM  rarely have any any continuity error  like like SWMM SWMM models do.
47:24
 I know  that also in the node results table, uh  you can also um take a look at the the  kind of the the continuity  uh error at each node as well.  Are you talking about ICM or or SWMM or  SWMM? Error with Yeah, with ICM.  Um just on that question.  Um Yeah, I ICM also has a simulation  summary report.  So, uh for example,  let's track them up.
47:59
 So, you can get this and get a report.  So, that that's another way to get an  overall mass balance. It gives you total  inflow, total outflow, and what was  stored there.  Okay.  Yep.  Um so, yeah, I guess one kind of blunt  question, um when do you recommend to  use ICM or SWMM engine, please?  Uh Do you recommend either or are there  certain cases where you recommend one  over the other?  Yeah, well, that that  given my history, that's that's  difficult to difficult to say. Yeah.
48:34
 Yeah, I mean, I I I think um we So,  yeah, we  we offer with with a regular ICM  license, you get both.  And um  in general, we, you know, we we we've  generally found that ICM can typically  run a little faster, and it has more  some more advanced options, especially  if you're going to be doing like  real-time modeling or advanced real-time  controls like VFDs, and so on.
48:57
 But, uh  there are still a lot of uh communities  in the US that do require to stick with  EPA SWMM because they'll have certain,  you know, uh um smaller contractors or  or smaller consultants that work with  them that um don't have the budget for a  full ICM license. And so, some  communities are kind of required to  stick with an open EPA SWMM model that  is freely, you know, accessible to all.
49:26
 And so, so, there are cases where we do  see users using SWMM within ICM.  Um we've also I've also seen some cities  actually using another SWMM solution, uh  um you know, like like InfoSWMM, XP  SWMM, you know, that there's other EPA  SWMMs out there, um but actually using  ICM as a central database  just because other SWMM models don't do  version control, data flags and scenario  management to the same degree that ICM  does.
49:56
 And I believe that that's been  another water talk in the past, but just  know that ICM can actually kind of  coexist alongside other SWMM platforms  because of the the ways that that Bob  was showing. You can manage a large  library of models within ICM that are  all integrated, connected with GIS, with  data flags, you know, tracking who  edited each one, and you can push out  the scenario and the version to EPA  SWMM, make changes, and you can bring  those back.
50:25
 Right. Yeah, the the data flags are  really really good in  InfoWorks ICM GUI, and they apply both  in in  InfoWorks ICM SWMM network and SWMM  or ICM SWMM. Yeah, it's confusing saying  the word  how many different times.  But, um  yeah, so we we wanted to be really we  want to basically have  this ICM GUI as like a  a really good database for all of your  SWMM related models or simulation  models.
50:55
 You get easily get data in and data out,  and don't no longer have to worry about  doing a lot of copying and pasting of  rainfall patterns, etc. So,  that that's really really easy to do.  And easy to do the comparisons. I will  say getting back to Nathan's original  question, ICM is a lot more robust  because it  has a lot of kind of neat features like  um  not allowing too long a pipe, breaking  the pipe up pipes up into smaller  smaller segments,  the automatic time stepping that  basically  goes down and then back up. Um it's a  lot easier to get a good answer than  SWMM 5 often because in SWMM 5 you need  to sometimes play with the options and  the time step especially.  So,  comparable answer.  Yeah.  Yeah, another comment on that is in  general the largest systems in the world
51:52
 all tend to use ICM engine. So. That's  that's also kind of telling.  Um let's see. There there was a  question. Um that I think I can answer  quick. Is the SWMM engine option  included in the ICM license one  procedure? So I I think I think this is  a question about ICM versus ICM one  which we've mentioned.
52:12
 So ICM one is a  licensed version where we take away the  multi-user aspect. But you still get all  the same engine features. So nothing is  different in in terms of engine. Um you  get SWMM or ICM engine in in any ICM  license. The only difference with ICM  one is we take away multi-user access as  well as remote simulation access.
52:36
 And we  make it uh a a subscription offering. So  you have to pay a subscription per year  for ICM one making it more affordable up  front. Um and you know in in some cases  it's that that makes it a a good choice  for consultants to consider. Um but  yeah.  So you know reach out to Innovyze sales  if if you're interested to learn more on  that.
53:01
 Um  Yeah, the log file actually tells you  if you're confused about which you're  using. You look at the log file and  it'll tell you either the SIM engine or  the SWMM SIM engine.  And both of those are included in one  SWMM and regular ICM.  Okay.  Sorry.  Um yeah, here here's a good one. There  is a base flow factor in ICM for  stability of the Saint Venant equations.
53:26
 Is this the same in SWMM?  Maybe can you can you talk about uh base  flow a little bit? Um  Yeah. Uh basically  um it's it's kind of covered in the  simulation parameters.  Uh here's the base flow here. So,  essentially ICM can't dry up. You can't  have a solution with um  no flow.  Um, there's something  kind of rudimentary it's a lot simpler,  but there's there's a minimum depth in  SWMM and set at 0.
53:57
0001  um, feet.  So, SWMM also doesn't  um  doesn't um, allow a dry  dry system. However, the the the the  dryness of SWMM SWMM 5 is a lot drier  than the than the base flow in in ICM.  So, basically ICM has kind of has like a  negative slot, I guess. No, not really.  But anyway, there's a lot of um  a lot of a lot of um,  base flow depths you can you can define.
54:26
 So, you're the if you're a user, you can  define what that base flow is and  there's a lot of um  features in ICM for basically taking out  that air that extra storage  and showing you what what's going on. I  don't know if I answered that question,  but good question.  I've actually uh, come across with like  force main pipes uh, because ICM  initializes and fills up the network  with water till a steady state is  achieved.
54:54
 Um, it it handles those force  mains a bit better uh, than SWMM which  will  unless unless you give it something, it  will start everywhere dry and it can  take a while to ramp and fill those  areas up and during that whole period  it's not  very stable. Um Yeah. Yeah, if uh, force  mains I especially for force mains in  SWMM  use a hot start file.
55:14
 Um, you're as as  Nathan says it could take a long time to  fill up those force mains  depending on the pump to turn on.  So, that works out there.  Yeah.  Um, so we've looked at nodes and pipes.  Can you show what a subcatchment looks  like? There's a question um, what does  the one SWMM catchment properties look  like? Is it the same as SWMM?  And  Yeah, do your models have subcatchments?  Yeah, yeah, they do.
55:45
 Yeah.  Yeah, obviously one of your many models.  There we go.  All right, so  Yeah, that's that's a good point.  Basically  it's swim five. So, there's the same  characteristics as subcatchment in swim  five. It has  three types of uh  surfaces. It has a impervious, pervious,  and a and a pervious without depression  storage.
56:12
 Um  infiltration models are the same. What  is different here well, was different  until Lou Rossman changed it, but  basically you  you you could have uh  and you you can't have in swim five now  different um infiltrations per  subcatchment.  So.  Curve number, modified green green green  amp, green amp, modified Horton, Horton,  etc.
56:37
 So, exactly the same same data. Now, if  I was to switch to um  ICM  network  and click here.  Uh  I don't know why it's up there.  Um oh, I see what happened what happened  there.  I must have converted it. Um basically  you just get the ICM network. So, if you  go over here to grid  and you look at the subcatchment data,  it's the ICM subcatchment data with the  runoff surface and the land use.
57:21
 If you were to go to um  uh swim and you look at the subcatchment  window  it's just the um  subcatchment data that's inside of swim  five. So, no extra data, looks exactly  like SWMM 5  um data. And then if you click over  here, it shows you uh those those  properties.  Okay.  All right, what's this extra quote?  Using ICM engine though.
57:48
 Uh yeah, yeah, another good question. Um  and this is actually a a suggestion that  we're working on when when you're  working on complex catchments, there are  a number of times that we face stability  issues due to a number of reasons. Maybe  be a good water topic on stabilities.  Um so so thanks for that comment and and  that's also a good a good suggestion for  for others.
58:07
 Feel free, you know, if if  you're if you struggle with a certain  aspect of your modeling, go ahead and  throw that in the chat and we can we're  always looking to add topics, but I know  we we are queuing up an upcoming topic  on ICM stability troubleshooting between  1D and 2D models.  So this sounds like maybe this is you  know, solving stability for 1D only  models.
58:32
 But yeah, those those are those are good  good inputs. Cuz  of course you know, in general you know,  we say ICM is going to be more robust  and it's going to be faster. There can  be of course times where ICM is not  stable due due to some model issues,  model problems that don't don't work  well with the engine and certainly an  ICM model can actually be slower  you know, if it if it's not configured  properly to to converge well.
58:56
 And so  generally what we see is a well-tuned  model can can run a lot faster than  SWMM. We didn't show any any  comparisons, but That brings up a really  key point. One of the key features of  ICM is has an initialization process.  So to even run an ICM model, you have to  basically initialize the whole model,  make sure everything's in balance, etc.
59:21
 before before running. So that that  basically  makes it like a super  hot start  before you even run. So, that's that's  pretty good.  Yeah, it comes up with your hot start  for you. Um  yeah.  Which initially I didn't like that, but  I've come to actually really like that  feature over time cuz  um  yeah, it's it's really helpful.
59:45
 Um  yeah, I guess one last question we can  touch on. Uh thanks for thanks for  staying on. We are kind of running out  of time. So, there's one last question.  What would be the rules for time step  selection in ICM engine? Does it follow  the current condition?  It follows the current condition. Um  it's pretty extensively covered in the  help file.
01:00:05
 So, basically, these are the  rules. So, for example, say you give it  a a max time step of 60 seconds. It goes  through the simulation and um it it it  does like what SWMM 5 does. It follows a  CFL and says, "Okay, I need to use a  10-second time step."  So, it does a 10-second time step and  finds out that certain nodes and certain  links do not converge.
01:00:26
 So, it says,  "Okay, I need to lower my time step down  to 5 seconds." Then it tries 5 seconds  and see if that converges. If that  doesn't converge, then it goes down to  2.5 seconds.  So, now it says, "Okay, at 2.5 seconds  it's converged. I'll use that for a  while." So, it'll use 2.5 seconds for a  while, then it'll say, "Okay, um I'm  converging really fast.
01:00:47
 I guess I could  increase my time step back up to 5  seconds." Then it goes 5 to 10, then  eventually back to back to 60. So, CFL  is key. However, it has this really nice  um time step having. So, if if it  doesn't converge, it lowers the time  step and then  makes it makes it more stable during  those  tricky uh um  peak flow  situations.
01:01:12
 Yeah. Yeah. I Yeah, my Yeah, my  understanding is it's not it's not fully  constrained by by CFL like SWMM engine  is. So, like if you have one short pipe,  it'll slow down the whole model. So long  as your flows are are are somewhat  steady, ICM can take much larger time  steps. It's just when you have these  Yeah, sharp time gradients of flow  spikes that then it does need to um  usually add some iterations.
01:01:34
 Yeah, if  you look at the ICM help, it you look at  the Prism um  box solution, it'll it'll talk about the  fact that ICM is implicit, so it can use  a lot longer than a CFL time step.  Yeah, thank you. Um yeah, thank thank  you Bob and thank you for for all the  questions that came in. Um in case I did  mix miss one or two, I'll take a look  back and I'll reach out to you.
01:02:00
 Um but yeah, thanks for for attending  and we look forward to seeing you again  in the future and reach out if you are  interested in presenting with us or if  you have topic ideas. Um we're always  always like the the the  the attendee feedback. So, thanks. Have  a good rest of the day.  Thank you, Nathan, and thank you,  attendees.
01:02:21
 Mhm.  Mhm.
