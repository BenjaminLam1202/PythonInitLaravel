import subprocess
import os
import time

ha1 ="@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ @@@@@@@@ @*#@@@@ @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@@  ,@.  @@ @@@@@    @(%@@@@    @@   @@ .  @@@@@.  @.@@@ @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@@& (@ @@ @ @@@@ @@@ @(%@@@@ @@@#&.@@(@ @@*@@@@ &&&&@.@ @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%#(((%&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#       ,#&@@@@@@@@@&%/        *@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%    &@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@    ,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@   .@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%   &@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.  (@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@/  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@@   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@  &@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  &@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  (@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@  @@@@@@@@@@@@@@@@@@@@@@@@@@@   *@@@@@@@@@@@@@@@@@(   @@@@@@@@@@@@  ,@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@  @@@@@@@@@@@@@@@@@@@@@@@@@@@,    @@@@@@@@@@@@@@@@@    .@@@@@@@@@@@@(  @@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@, *@@@@@@@@@@@@@@@@&&&&&&&&%&&&@@@@@@@@@@@@@@@@@@@@@@@@@&&&&&&&&&&&&@@@   @@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@  @@@@@@@@@@@@@@@@@&&&&&&&&&&&&@@@@@@@@@@@@@@@@@@@@@@@@@&&&&&&&&&&&&@@@@@  @@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@    (@@@@@@.   @@@@@@@@@@@@@@@@@@@@@@&  @@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#*,*/&@@@@@@@@@@@@@@@@@@@@@@@@@@@  @@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@  &@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  @@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  (@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  ,@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@/  @@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@@   %@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@   @@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*     #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&.     .@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@   /&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  @@@@@@@@@@@  #@@@@@@@@@@* .@@@  &@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  @@@@@@@@@@@* ,@@@@@@@@@@@  @@@  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@. .@@@@(  @@@@@  &@@@@@@@@@. *@@@  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@(  @@@@@@.  @@@@@/  &@@@@@@%  @@@  (@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  @@@@@@@@@   @@@@@%  @@@@@  @@@  ,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&  @@@@@@@@@@@&         ,@@@@    .@.  &@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@##  ,          @@@@@@@@@@  @@@@@@@@@@%  #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@###%##  @@@@@@@@@@@@@@@@@@@@  @@@@@@@@@   %####@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@######.      *(%&&&&%/               .%######@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%######%#%%%%%%%#%###%%%%#####%%##@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n"
ha2 ="MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWNXXXXXXXXNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWN0kxdoooooooooooooooooxOKNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWKxooodxOKXNWWWMMMMMWWNK0kxollox0NMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMXxlldOXWMMMMMMMMMMMMMMMMMMMMMMWXOoccdKWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMXxclONMMWMMMMMMMMMMMMMMMMMMMMMMMMMMMN0o:l0WMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWOcl0WWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWKd:oXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNd:xNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMW0c:0MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNd:OWMMMMMMWWMWWMMMMMMMMMMMMMWWMMMMMMMMMMMMMMMXc:0MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWx;kWMMMMMW0lcOWWMMMMMMMMMNxcdKWMMMMMMMMMMMMMMMMXc:KMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWXo:kWWWWWWNNx..oNWMMMMMMMMMKc.;ONNNWWWWMMMMMMMMMMMO;dWMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWO:l0WWXKKKKKK0ddXMWWMMMMMWNWW0okKKKKKKXXWMMMMMMMMMMNc:XMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMO;oNMMWWNNNNNNXkxXWXxoddoooxXW0dONNNNNNNNWMMMMMMMMMMWo;0MMMMMMMMMMMMMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNc:XMMMMMMMMMMWNkxXWWX0OO00KNWW0d0WWMMMMMMMMMMMMMMMMMWo;KMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWMX:cNMMMMMMMMMMWNkkXWMMMMMMMMMMWKk0WMMMMMMMMMMMMMMMMMMNccXMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWWd;OMMMMMMMMMMMN00NWMMMMMMMMMMMWNWMMMMMMMMMMMMMMMMMMWx,xWMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMXo:OWMMMMMMMMWNOONWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWWk;oNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNxclONMMMMMMWWNNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMW0l;xNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWXxllox0NWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWN0dccdKWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWXOdllooodxOXWMMMMMMMMMMMMMMMMMMMMN0kdollloONMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNX0Oko,lNMWWMMMMMMMMNNMMMMMMMk,cdk0XWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMXccNXoxWMMMMMMNodWMMMMMMd;OMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNc:XK:lNMMMMMWx;kWW0xKMMx,kMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWd,kWx;kWMMW0l:kNW0:lXMM0;lNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWO,;00::XNKx,cKX0ocxXMMMWo;OMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWk:looolkOc,:cloooxXWWWMWWk,xMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWXc,0WWWWWl;xKWNXNWMMNOdodd:,xNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWXOd::loxxk:.'cOKNWNNNX0xl:.'okkKWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWXK0kdlcccccc::ccllllcccccok0KXNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWWNNNXXXXXKKKKKKKXXNNNWWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\n"
print (ha1)
user="hilton@asia.cybridge.jp"
pas ="BenjaminLam123"
name ="huy"
print(os.getcwd())



you = raw_input("what you want bruh??? ")
print(you)



if "make folder" in you:
	robot_brain = "nice \"First commit\""
	print (robot_brain)
	project_name = raw_input("what yours project name bruh??? ")
	robot_do_2 = "cd"+"\n"+"cd " +os.getcwd()+"\n"+"cd "+project_name
	path = os.getcwd()+"/"+project_name
	if os.path.exists(path):
		folder_name = raw_input("what do you want yours folder in your project name bruh??? ")
		robot_do_3 = "cd"+"\n"+"cd " +os.getcwd()+"\n"+"mkdir "+project_name+"/"+folder_name
		subprocess.Popen(robot_do_3, shell=True, stdout=subprocess.PIPE).stdout.read()
	else:
		folder_name = raw_input("what do you want yours new folder name bruh??? ")
		robot_do_3 = "cd"+"\n"+"cd " +os.getcwd()+"\n"+"mkdir "+folder_name
		subprocess.Popen(robot_do_3, shell=True, stdout=subprocess.PIPE).stdout.read()
		robot_brain = "done yours new folder is "+folder_name
		print (robot_brain)
elif "git" in you:
	robot_brain = "nice git"
	print (robot_brain)
	project_name = raw_input("what yours project name bruh??? ")
	robot_do_2 = "cd"+"\n"+"cd " +os.getcwd()+"\n"+"cd "+project_name
	path = os.getcwd()+"/"+project_name
	if os.path.exists(path):
		git_already = raw_input("git yet?[y/n] ")
		if git_already == "y":
			commit = raw_input("what yours commit name bruh??? ")
			robot_do_3 = "cd"+"\n"+"cd " +os.getcwd()+"\n"+"cd "+project_name+"\n"+"git add ."+"\n"+"git commit -m \""+commit+"\""+"\n"+"git push -u -f origin master "+"\n"
			subprocess.Popen(robot_do_3, shell=True, stdout=subprocess.PIPE).stdout.read()
			robot_brain = "done"
			print (robot_brain)
		elif git_already == "n":
			path = raw_input("what yours path name bruh??? ")
			robot_do_3 = "cd"+"\n"+"cd " +os.getcwd()+"\n"+"cd "+project_name+"\n"+"git init"+"\n"+"git config --global user.email "+"\n"+user+"\""+"\n"+"git config --global user.email "+name+"\""+"\n"+"git add ."+"\n"+"git commit -m \"first commit\""+"\n"+"git remote add origin "+path+"\n"+"git push -u origin master"
			subprocess.Popen(robot_do_3, shell=True, stdout=subprocess.PIPE).stdout.read()		
			robot_brain = "done"
elif "laravel" in you:
	robot_brain = "nice laravel project"
	print (robot_brain)
	project_name = raw_input("what yours laravel project name bruh??? ")
	robot_do_2 = "cd"+"\n"+"cd " +os.getcwd()+"\n"+"cd "+project_name
	path = os.getcwd()+"/"+project_name
	if os.path.exists(path):
		robot_brain = "already exists"
		print (robot_brain)
	else:
		robot_do_3 = "cd " +os.getcwd()+"\n"+"composer create-project --prefer-dist laravel/laravel "+project_name+"\n"
		subprocess.Popen(robot_do_3, shell=True, stdout=subprocess.PIPE).stdout.read()	
		robot_do_3 = "cd " +os.getcwd()+"\n"+"chown -R apache.apache " +os.getcwd()+"/"+project_name+"\n"+"chmod -R 755 " +os.getcwd()+"/"+project_name+"\n"+"chmod -R 755 " +os.getcwd()+"/"+project_name+"/storage"+"\n"
		subprocess.Popen(robot_do_3, shell=True, stdout=subprocess.PIPE).stdout.read()		
		robot_do_4 = "cd " +os.getcwd()+"/"+project_name+"\n"+"cp .env.example .env"+"\n"
		subprocess.Popen(robot_do_4, shell=True, stdout=subprocess.PIPE).stdout.read()
		time.sleep(1)			
		robot_do_5 = "cd " +os.getcwd()+"/"+project_name+"\n"+"php artisan key:generate"+"\n"
		subprocess.Popen(robot_do_5, shell=True, stdout=subprocess.PIPE).stdout.read()	
		time.sleep(2)			
		robot_brain = "done your project laravel is "+project_name
		print (robot_brain)
		intro = "\nvim /etc/httpd/conf/httpd.conf\n\n\n\n<VirtualHost *:80>\n       ServerName laravel.example.com\n       DocumentRoot /var/www/laravel/public\n       <Directory /var/www/laravel>\n              AllowOverride All\n       </Directory>\n</VirtualHost>\n\n\n\nservice httpd restart"
		print (intro)
elif "larain" in you:
	robot_brain = "install laravel"
	print (robot_brain)
	project_name = raw_input("are you sure you wanna install laravel and composer ?????[yes/no] ")
	robot_do_2 = "cd"+"\n"+"cd " +os.getcwd()+"\n"+"cd "+project_name
	print (project_name)
	if "no" in project_name:
		robot_brain = "fuck you bro!!!"
		print (robot_brain)
	elif "yes" in project_name:
		line1 = "cd " +os.getcwd()+"\n"+"sudo curl -sS https://getcomposer.org/installer | php "+"\n"
		subprocess.Popen(line1, shell=True, stdout=subprocess.PIPE).stdout.read()
		time.sleep(20)				
		line2 = "sudo mv composer.phar /usr/bin/composer "+"\n"
		subprocess.Popen(line2, shell=True, stdout=subprocess.PIPE).stdout.read()			
		line3 = "sudo chmod +x /usr/bin/composer"+"\n"
		subprocess.Popen(line3, shell=True, stdout=subprocess.PIPE).stdout.read()							
		line5 = "composer"+"\n"
		time.sleep(4)	
		subprocess.Popen(line5, shell=True, stdout=subprocess.PIPE).stdout.read()			
		robot_brain = raw_input("done install composer , do you want to make your first laravel project[yes/no] ")
		print (robot_brain)		
		if "yes" in robot_brain:
			project_name = raw_input("what yours laravel project name bruh??? ")
			robot_do_2 = "cd"+"\n"+"cd " +os.getcwd()+"\n"+"cd "+project_name
			path = os.getcwd()+"/"+project_name
			if os.path.exists(path):
				robot_brain = "already exists"
				print (robot_brain)
			else:
				robot_do_3 = "cd " +os.getcwd()+"\n"+"composer create-project --prefer-dist laravel/laravel "+project_name+"\n"
				subprocess.Popen(robot_do_3, shell=True, stdout=subprocess.PIPE).stdout.read()	
				robot_do_3 = "cd " +os.getcwd()+"\n"+"chown -R apache.apache " +os.getcwd()+"/"+project_name+"\n"+"chmod -R 755 " +os.getcwd()+"/"+project_name+"\n"+"chmod -R 755 " +os.getcwd()+"/"+project_name+"/storage"+"\n"
				subprocess.Popen(robot_do_3, shell=True, stdout=subprocess.PIPE).stdout.read()		
				robot_do_4 = "cd " +os.getcwd()+"/"+project_name+"\n"+"cp .env.example .env"+"\n"
				subprocess.Popen(robot_do_4, shell=True, stdout=subprocess.PIPE).stdout.read()
				time.sleep(2)			
				robot_do_5 = "cd " +os.getcwd()+"/"+project_name+"\n"+"php artisan key:generate"+"\n"
				subprocess.Popen(robot_do_5, shell=True, stdout=subprocess.PIPE).stdout.read()	
				time.sleep(2)			
				robot_brain = "done your project laravel is "+project_name
				print (robot_brain)
				intro = "\nvim /etc/httpd/conf/httpd.conf\n\n\n\n<VirtualHost *:80>\n       ServerName laravel.example.com\n       DocumentRoot /var/www/laravel/public\n       <Directory /var/www/laravel>\n              AllowOverride All\n       </Directory>\n</VirtualHost>\n\n\n\nservice httpd restart"
				print (intro)
		elif "no" in robot_brain:
			robot_brain = "fuck you bro!!!"
			print (robot_brain)
elif you == "":
	robot_brain = "bye bro"	
	print (ha2)
	print (robot_brain)


