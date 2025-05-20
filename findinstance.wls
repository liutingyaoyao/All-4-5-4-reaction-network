#!/usr/bin/env wolframscript
(* ::Package:: *)

FindInstance[12*h1^3*h2^2*h3*\[Lambda]^6 + 3*h1^3*h2^2*h4*\[Lambda]^6 + 4*h1^3*h2*h3^2*\[Lambda]^6 +4*h1^3*h2*h3*h4*\[Lambda]^6 
+ h1^3*h2*h4^2*\[Lambda]^6 + h1^3*h3^2*h4*\[Lambda]^6 + h1^3*h3*h4^2*\[Lambda]^6 + 24*h1^2*h2^3*h3*\[Lambda]^6 + 6*h1^2*h2^3*h4*\[Lambda]^6 + 
12*h1^2*h2^2*h3^2*\[Lambda]^6 + 9*h1^2*h2^2*h3*h4*\[Lambda]^6 + 4*h1^2*h2^2*h4^2*\[Lambda]^6 + 4*h1^2*h2*h3^3*\[Lambda]^6 + 4*h1^2*h2*h3^2*
h4*\[Lambda]^6 + 2*h1^2*h2*h3*h4^2*\[Lambda]^6 + h1^2*h2*h4^3*\[Lambda]^6 + h1^2*h3^3*h4*\[Lambda]^6 +2*h1^2*h3^2*h4^2*\[Lambda]^6 + h1^2*h3*h4^3*\[Lambda]^6 
+ 16*h1*h2^3*h3^2*\[Lambda]^6 - 12*h1*h2^3*h3*h4*\[Lambda]^6 + 8*h1*h2^2*h3^3*\[Lambda]^6 + 6*h1*h2^2*h3^2*h4*\[Lambda]^6 - 
12*h1*h2^2*h3*h4^2*\[Lambda]^6 + 2*h1*h2*h3^3*h4*\[Lambda]^6 + h1*h2*h3^2*h4^2*\[Lambda]^6 - 3*h1*h2*h3*h4^3*\[Lambda]^6 + 
h1*h3^3*h4^2*\[Lambda]^6 + h1*h3^2*h4^3*\[Lambda]^6==0&&h1>0&&h2==1&&h3==1/2&&h4==1&&\[Lambda]==1,{\[Lambda],h4,h3,h2,h1},Reals]



