#!/bin/sh
# code by madun modsメ
# script perubah tampilan termux

# tampilan
tamp1="==============================="
tamp2=" {      WELCOME TO TERMUX     }

# login termux
toilet -f big -f gay LOGIN
echo "Masukkan Password" | lolcat
read pass

# data tampilan
if [ $pass = hacker ]
then
  echo"masukkan title"
  read title
 clear
  figlet $title | lolcat
  echo $tam1 | lolcat # tampilan 1
  echo $tam2 | lolcat # tampilan 2
  echo $tam1 | lolcat # tampilan 1
  echo
   echo "# DDOS cyber" | lolcat
   echo "# Scurity punk" | lolcat
   echo "# Mafia teknonogi" | lolcat
     echo $tam1 | lolcat # tampilan 1
     else
       echo "Password salah" | lolcat
        echo $tam1 | lolcat # tampilan 1
        sh.tampilan.sh
   fi