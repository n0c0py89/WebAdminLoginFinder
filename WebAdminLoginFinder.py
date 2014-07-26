'''
Module name: WebAdminLoginFinder.py
Author: Chrystz aka Newton
Contact: blood4thirst@gmail.com
Desc: Finds the administrative login page for various web application
Version: 3.0
Release Date: 1.17.14
'''
print "Web Administration login page finder Version 3.0"
print "Author: Chrystz aka Newton"
print "Please report any bug that you find to blood4thirst@gmail.com \n"

import httplib
import urllib2
import sys
import socket
import os
import urlparse
import re

try:

    php = [
	'admin-login.php', 'admin.php', 'administrator/index.html', 
	'authadmin.php', 'cp.html', 'login_out/', 'admin/', 'signin/', 
	'administrator.html', 'control/', 
	'panel-administracion/index.html', 'pages/admin/admin-login.php',
	'banneradmin/', 'admincp/index.html', 'users/', 'bigadmin/', 
	'login/', 'super_indexphp', 'sys-admin/', 'manage.php', 
	'adm/index.php', 'home.html', 'userlogin.php', 'manager/', 
	'navSiteAdmin/', 'kpanel/', 'panel/', 'admin2.php', 
	'admin_area.php', 'home.php', 'adminitems/', 
	'admin/controlpanel.htm', 'Indy_admin/', 'irc-macadmin/', 
	'adm.html', 'webadmin/admin.php', 'superuser/', 
	'panel-administracion/login.php', 'admin/cp.php', 'login1/', 
	'administrator/login.php', 'panel-administracion/index.php', 
	'wp-login.php', 'admincontrol.html', 'sshadmin/', 'login.html',
	'login_db/', 'admin/login.html', 'supervise/', 'showlogin/', 
	'member.php', 'project-admins/', 'admin/admin-login.html', 
	'newsadmin/', 'hpwebjetadmin/', 'radmind-1/', 'administr8.php', 
	'cpanel_file/', 'panel-administracion/admin.php', 'acceso.php', 
	'modelsearch/index.html', 'sign-in.php', 'bb-admin/', 
	'moderator/login.html', 'webadmin.html', 'control.php', 
	'superman/', 'authentication.php', 'user/', 'accounts/', 
	'webmaster.php', 'members/', 'secrets/', 'sign-in/', 
	'adm/admloginuser.php', 'login.htm', 'moderator/admin.html', 
	'admincp/', 'adminpanel.html', 'super1php', 
	'administrator/login.html', 'phpldapadmin/', 
	'ServerAdministrator/', 'bb-admin/login.php', 
	'admin/admin_login.php', 'logout/', 'checklogin.php', 
	'members.php', '0admin/', 'adminitems.php', 'admin1.php', 
	'adminarea/index.php', 'Server/', 'ur-admin/', 'sysadm.php', 
	'signin.php', 'admin2/', 'admin2.html', 'log_in.php', 
	'webadmin.php', 'user.php', 'ccp14admin/', 
	'admincontrol/login.html', 'webadmin/login.html', 'auth.php', 
	'admin1/', 'administr8/', 'superuserphp', 'meta_login/', 
	'login_outphp', 'admincontrol/', 'sysadmin.php', 'check.php', 
	'cadmins/', 'administratorlogin/', 'adm/index.html', 'smblogin/',
	'siteadmin/login.html', 'login_userphp', 'controlpanel/', 
	'administratie/', 'member/', 'Super-Admin/', 'log-in/', 
	'user.html', 'login_adminphp', 'bb-admin/admin.html', 
	'memberadmin/', 'administration/', 'admin/home.html', 
	'relogin.html', 'adminpro/', 'adminitem/', 'bb-admin/login.html',
	'admin/adminLogin.html', 'administrator/account.html', 
	'supervisor/', 'authenticate.php', 'sign_in/', 'root/', 
	'admin2/index.php', 'moderator/', 'pages/admin/', 'login1php', 
	'logoutphp', 'adminlogin.php', 'wp-admin/', 'admins.php', 
	'server_admin_small/', 'adminarea/admin.php', 'admin/admin.php', 
	'admincp/index.asp', 'security/', 
	'panel-administracion/admin.html', 'bb-admin/admin.php', 
	'admin1.htm', 'loginsuper/', 'cmsadmin/', 'pgadmin/', 
	'login_admin/', 'admincontrol/login.php', 'radmind/', 
	'ur-admin.php', 'LiveUser_Admin/', 'admin_area/', 
	'modules/admin/', 'admincp/login.asp', 'admin.htm', 
	'supervise/Loginphp', 'admin/admin-login.php', 'siteadmin/', 
	'adminarea/login.php', 'panel.php', 'SysAdmin2/', 'loginsave/', 
	'access/', 'modelsearch/admin.php', 'admin/login.php', 
	'pureadmin/', 'ss_vms_admin_sm/', 'PSUser/', 
	'adminarea/index.html', 'yonetici.html', 'access.php', 'vorud/', 
	'adminLogin/', 'admin/account.php', 'adminpanel/', 'isadmin.php',
	'yonetici.php', 'loginerror/', 'bb-admin/index.html', 
	'admin/index.php', 'secret/', 'Server.php', 'loginsuperphp', 
	'administrators/', 'admin/cp.html', 'nsw/admin/login.php', 
	'admin/home.php', 'cmsadmin.php', 'admin.html', 
	'admin/adminLogin.php', 'usr/', 'admin_area/login.html', 
	'log-in.php', 'sysadm/', 'user/admin.php', 
	'rcjakar/admin/login.php', 'bbadmin/', 'webadmin/index.html', 
	'relogin.php', 'moderator/login.php', 'secure/', 'letmein/', 
	'fileadmin/', 'simpleLogin/', 'login-redirect/', 'cp.php', 
	'admin4_colon/', 'admin_area/index.php', 'globes_admin/', 
	'system_administration/', 'usuario/', 'adminitem.php', 
	'processlogin.php', 'management/', 'admin/index.html', 
	'panel-administracion/', 'admin_area/admin.html', 
	'adminLogin.html', 'Database_Administration/', 'vmailadmin/', 
	'checkuser.php', 'adminsite/', 'siteadmin/login.php', 
	'wizmysqladmin/', 'administrator.php', 'staradmin/', 
	'pages/admin/admin-login.html', 'typo3/', 'vorod.php', 
	'adminarea/admin.html', 'admins/', 'UserLogin/', 'phppgadmin/', 
	'cpanel/', 'admin_area/admin.php', 'Lotus_Domino_Admin/', 
	'loginok/', 'admin2/login.php', 'adminarea/login.html', 
	'siteadmin.php', 'myadmin/', 'superuser.php', 'vadmind/', 
	'sysadmins/', 'manage/', 'acct_login/', 'modelsearch/login.html',
	'adminLogin.php', 'uvpanel/', 'administrivia/', 'superphp', 
	'loginphp', 'SysAdmin/', 'usuarios/login.php', 
	'bb-admin/index.php', 'phpmyadmin/', 'affiliate.php', 
	'authuser.php', 'webadmin/index.php', 'customer_login/', 
	'admloginuser.php', 'supermanphp', 'loginflat/', 'administrator/'
	, 'aadmin/', 'users.php', 'admin5/', 'yonetim.html', 
	'admin/controlpanel.php', 'autologin/', 'modelsearch/login.php', 
	'super1/', 'super_loginphp', 'supermanagerphp', 
	'admin/admin_login.html', 'phpSQLiteAdmin/', 'log_in/', 
	'sql-admin/', 'admin4_account/', 'login-us/', 'openvpnadmin/', 
	'admin_area/login.php', 'vorud.php', 'registration/', 
	'controlpanel.html', 'utility_login/', 
	'administrator/account.php', 'usuarios/', 'admin_login.php', 
	'ezsqliteadmin/', 'webmaster/', 'vorod/', 'useradmin/', 
	'logo_sysadmin/', 'administratorlogin.php', 
	'admin/controlpanel.html', 'users/admin.php', 'cp/', 
	'admin/adminLogin.htm', 'siteadmin/index.php', 'support_login/', 
	'adm.php', 'administrators.php', 'accounts.php', 'moderator.php',
	'controlpanel.php', 'AdminTools/', 'admin_login.html', 
	'account.php', 'cgi-bin/loginphp', 'moderator/admin.php', 
	'admin/login.htm', 'login.php', 'management.php', 'blogindex/', 
	'webadmin/admin.html', 'instadmin/', 'sign_in.php', '0manager/', 
	'sub-login/', 'power_user/', 'administer/', 
	'administratoraccounts/', 'platz_login/', 'admin/account.html', 
	'fileadmin.php', 'memberadmin.php', 'adm/', 'manuallogin/', 
	'blog/wp-login.php', 'administrator/index.php', 'xlogin/', 
	'adminarea/', 'panel-administracion/login.html', 
	'admincontrol.php', 'checkadmin.php', 'wp-login/', 
	'admincp/login.php', 'adminpanel.php', 'relogin.htm', 'rcLogin/',
	'autologin.php', 'formslogin/', 'yonetim.php', 
	'admin-login.html', 'account.html', 'adm_auth.php', 'admin3/', 
	'dir-login/', 'admin/admin.html', 'directadmin/', 'webadmin/', 
	'letmein.php', 'modelsearch/admin.html', 'admin4/', 'memlogin/', 
	'moderator.html', 'system-administration/', 'webadmin/login.php',
	'manager.php', 'admin_area/index.html', 'macadmin/', 
	'modelsearch/index.php', 'admin1.html', 'administration.php'
	]

    asp = [
	'panel-administracion/admin.html', 'members/', 'admin/cp.html', 
	'siteadmin/login.html', 'ezsqliteadmin/', 'adminitem/', 
	'supermanasp', 'loginsuperasp', 'adminarea/admin.asp', 
	'authadmin.asp', 'login.html', 'modules/admin/', 'administratie/'
	, 'adm/index.asp', 'isadmin.asp', 'instadmin/', 'login_adminasp',
	'panel-administracion/login.asp', 'adm/index.html', 
	'login_outasp', 'wp-admin/', 'Database_Administration/', 'usr/', 
	'login.asp', 'admin_area.asp', 'admin/adminLogin.html', 
	'ur-admin/', 'administratoraccounts/', 'admin/login.htm', 
	'admin/', 'home.html', 'webmaster/', 'wp-login.php', 'adminarea/'
	, 'administrator/index.asp', 'signin/', 'vorud/', 'home.asp', 
	'admin_area/', 'users.asp', 'panel.asp', 
	'panel-administracion/admin.asp', 'cadmins/', 
	'modelsearch/index.html', 'superasp', 'user/', 'meta_login/', 
	'Server/', 'bb-admin/', 'siteadmin/index.asp', 'secret/', 
	'admincp/index.asp', 'admin/index.html', 'SysAdmin/', 
	'acct_login/', '0admin/', 'letmein.asp', 'loginsuper/', 
	'administrator/login.asp', 'admin1.htm', 'vadmind/', 
	'admin_login.asp', 'Indy_admin/', 'utility_login/', 'accounts/', 
	'UserLogin/', 'authenticate.asp', 'sign_in/', 'webmaster.asp', 
	'login1/', 'supervisor/', 'webadmin/login.html', 
	'admin-login.asp', 'sshadmin/', 'loginflat/', 'sys-admin/', 
	'administrator.asp', 'login_admin/', 'sign-in.asp', 
	'adminarea/index.html', 'admincontrol/login.asp', 'adminsite/', 
	'management.asp', 'yonetici.html', 'users/admin.asp', 
	'system-administration/', 'moderator.asp', 'dir-login/', 
	'irc-macadmin/', 'account.html', 'admin/admin.html', 
	'modelsearch/index.asp', 'login/', 'bb-admin/login.asp', 
	'member.asp', 'user.asp', 'control.asp', 
	'pages/admin/admin-login.asp', 'webadmin/admin.html', 
	'hpwebjetadmin/', 'moderator/', 'administrator/account.asp', 
	'cgi-bin/loginasp', 'accounts.asp', 'sysadmin.asp', 'cpanel/', 
	'directadmin/', 'adminarea/index.asp', 'admin/account.asp', 
	'cp.html', 'yonetim.html', 'admin2/', 'power_user/', 
	'admin4_colon/', 'superuserasp', 'wp-login/', 'webadmin.html', 
	'administrivia/', 'admin/login.html', 'supermanagerasp', 
	'yonetici.asp', 'administrator/', 'PSUser/', 'vorud.asp', 
	'customer_login/', 'adminLogin.html', 
	'administrator/account.html', 'log-in.asp', 'phpldapadmin/', 
	'logout/', 'administr8.asp', 'admin/admin-login.html', 
	'admin_area/login.asp', 'moderator/admin.html', 'adminpanel.html'
	, 'security/', 'admincp/login.asp', 'login-redirect/', 
	'admin_area/admin.html', 'system_administration/', 
	'admin/index.asp', 'adm_auth.asp', 'user.html', 
	'admin/admin-login.asp', 'moderator/admin.asp', 'manuallogin/', 
	'admin5/', 'administrators/', 'login.htm', 'cp/', 
	'webadmin/index.asp', 'myadmin/', 'webadmin/login.asp', 
	'modelsearch/login.asp', 'vorod/', 'administrator/login.html', 
	'adminLogin.asp', 'autologin.asp', 'webadmin.asp', 
	'wizmysqladmin/', 'admin2/index.asp', 'administr8/', 
	'modelsearch/admin.html', 'control/', 'manage.asp', 'users/', 
	'admin/login.asp', 'adm/admloginuser.asp', 'phpSQLiteAdmin/', 
	'admin/admin.asp', 'AdminTools/', 'radmind-1/', 'typo3/', 
	'bb-admin/admin.html', 'admin.html', 'ur-admin.asp', 
	'administration.asp', 'bb-admin/index.html', 'openvpnadmin/', 
	'bb-admin/admin.asp', 'siteadmin.asp', 'Super-Admin/', 
	'globes_admin/', 'navSiteAdmin/', 'admin.asp', 'sub-login/', 
	'log-in/', 'admin_area/index.html', 'autologin/', 'adminLogin/', 
	'administer/', 'pgadmin/', 'login_out/', 
	'panel-administracion/index.html', 'admin1.asp', 'kpanel/', 
	'admin1/', 'uvpanel/', 'supervise/Loginasp', 'cmsadmin/', 
	'administratorlogin/', 'pureadmin/', 'adminitems.asp', 
	'modelsearch/login.html', 'admin_area/index.asp', 'check.asp', 
	'checkadmin.asp', 'adminarea/admin.html', 'yonetim.asp', 
	'manager/', 'admincontrol/', 'fileadmin/', 'adm.html', 'manage/',
	'showlogin/', 'admin2.html', 'server_admin_small/', 'login1asp',
	'admins/', 'login_userasp', 'admin/adminLogin.asp', 
	'relogin.html', 'letmein/', 'admin/account.html', 'rcLogin/', 
	'moderator/login.html', 'adminpanel/', 'admin/home.html', 
	'superuser/', 'admin1.html', 'simpleLogin/', 'administrators.asp'
	, 'administrator/index.html', 'fileadmin.asp', 'panel/', 
	'super1asp', 'moderator.php', 'bb-admin/login.html', 'sysadmins/'
	, 'newsadmin/', 'signin.asp', 'adm.asp', 'super1/', 'cp.asp', 
	'admincontrol.html', 'management/', 'vorod.asp', 
	'admin/admin_login.html', 'access/', 'adminpanel.asp', 'adm/', 
	'adminarea/login.html', 'admin/controlpanel.htm', 'userlogin.asp'
	, 'secrets/', 'super_indexasp', 'panel-administracion/', 
	'admin_area/login.html', 'adminpro/', 'admin/admin_login.asp', 
	'admin/controlpanel.html', 'bbadmin/', 'ss_vms_admin_sm/', 
	'support_login/', 'controlpanel.asp', 'macadmin/', 'phppgadmin/',
	'checklogin.asp', 'loginok/', 'registration/', 'relogin.htm', 
	'panel-administracion/index.asp', 'authuser.asp', 
	'authentication.asp', 'relogin.asp', 'administratorlogin.asp', 
	'memlogin/', 'modelsearch/admin.asp', 'admincontrol.asp', 
	'webadmin/index.html', 'admin4/', 'adminlogin.asp', 'log_in.asp',
	'admin3/', 'ServerAdministrator/', 'memberadmin/', 'auth.asp', 
	'logoutasp', 'memberadmin.asp', 'pages/admin/', 'blogindex/', 
	'admin_login.html', 'member/', 'admin2/login.asp', 
	'admincp/index.html', 'administration/', 'adminitem.asp', 
	'panel-administracion/login.html', 'xlogin/', 'blog/wp-login.asp'
	, 'login_db/', 'project-admins/', 'pages/admin/admin-login.html',
	'useradmin/', 'admincontrol/login.html', 'banneradmin/', 
	'Lotus_Domino_Admin/', 'sql-admin/', 'processlogin.asp', 
	'aadmin/', 'superuser.asp', 'platz_login/', 'SysAdmin2/', 
	'moderator/login.asp', 'controlpanel.html', 'smblogin/', 
	'cpanel_file/', 'admincp/', 'bb-admin/index.asp', 'siteadmin/', 
	'admin4_account/', 'admloginuser.asp', 'admin-login.html', 
	'sign_in.asp', 'admin_area/admin.asp', 'Server.asp', 
	'webadmin/admin.asp', 'loginerror/', '0manager/', 'webadmin/', 
	'LiveUser_Admin/', 'siteadmin/login.asp', 'vmailadmin/', 
	'admin/home.asp', 'sysadm/', 'loginasp', 'access.asp', 
	'adminarea/login.asp', 'members.asp', 'administrator.html', 
	'supervise/', 'controlpanel/', 'superman/', 'admin/cp.asp', 
	'login-us/', 'adminitems/', 'ccp14admin/', 'admin.htm', 'root/', 
	'sign-in/', 'cmsadmin.asp', 'radmind/', 'super_loginasp', 
	'logo_sysadmin/', 'admin/controlpanel.asp', 'loginsave/', 
	'log_in/', 'admin/adminLogin.htm', 'admins.asp', 'manager.asp', 
	'formslogin/', 'checkuser.asp', 'bigadmin/', 'affiliate.asp', 
	'admin2.asp', 'account.asp', 'sysadm.asp', 'acceso.asp', 
	'user/admin.asp', 'staradmin/', 'secure/', 'moderator.html'
	]

    jsp = [
	'admin2/index.jsp', 'admincontrol/login.js', 
	'admin4_colon/', 'admin/admin-login.html', 'showlogin/', 
	'memlogin/', 'system-administration/', 'Indy_admin/', 
	'checkuser.js', 'directadmin/', '0admin/', 'admin1.js', 'cp/', 
	'pureadmin/', 'userlogin.js', 'vorod.js', 'admin/admin_login.jsp'
	, 'sysadm.jsp', 'memberadmin.js', 'admin.html', 'control.js', 
	'webadmin.html', 'panel-administracion/index.js', 
	'controlpanel.html', 'letmein.jsp', 'adminarea/login.js', 
	'panel-administracion/admin.js', 'pgadmin/', 'admin1/', 
	'acct_login/', 'admin_area/admin.jsp', 'administrator.jsp', 
	'authadmin.jsp', 'administrator/', 'admin/admin_login.html', 
	'userlogin.jsp', 'admin/controlpanel.htm', 
	'admin/adminLogin.html', 'aadmin/', 'loginjsp', 
	'admincp/index.asp', 'bigadmin/', 'admincontrol/login.html', 
	'administrators.jsp', 'home.jsp', 'webmaster/', 'authuser.js', 
	'account.html', 'radmind-1/', 'irc-macadmin/', 'admins.js', 
	'bb-admin/admin.jsp', 'manager.jsp', 'customer_login/', 
	'autologin.js', 'user.js', 'adminpanel.jsp', 'supermanagerjs', 
	'admin.js', 'super_indexjsp', 'affiliate.js', 
	'modelsearch/index.js', 'administration/', 'PSUser/', 
	'superuserjsp', 'admin4/', 'adm_auth.jsp', 'auth.js', 
	'admloginuser.jsp', 'accounts/', 'loginjs', 'admin2/login.jsp', 
	'admin_area/login.jsp', 'control.jsp', 'sysadmins/', 'access.js',
	'modelsearch/login.html', 'admin/home.js', 'admin_area.js', 
	'admloginuser.js', 'cp.html', 'admin/home.html', 'adm/index.html'
	, 'admin/adminLogin.js', 'siteadmin/login.html', 'support_login/'
	, 'users.js', 'vorud.js', 'adm/admloginuser.jsp', 'superuser/', 
	'adminitems/', 'siteadmin/login.js', 'users/admin.jsp', 
	'administr8.js', 'smblogin/', 'admin_area/index.html', 
	'ur-admin.jsp', 'platz_login/', 'phpSQLiteAdmin/', 
	'pages/admin/admin-login.html', 'authenticate.js', 'member.jsp', 
	'admin/controlpanel.html', 'admin-login.html', 'admin/login.htm',
	'secure/', 'checklogin.jsp', 'login_admin/', 'admin_login.jsp', 
	'sign-in.js', 'administratoraccounts/', 'log_in/', 
	'adm/admloginuser.js', 'supervisor/', 'admin_area/', 
	'admin_area/index.js', 'processlogin.js', 'adminarea/index.js', 
	'panel-administracion/index.html', 'loginsuper/', 'sign-in/', 
	'supervise/Loginjs', 'user/admin.jsp', 'admin/admin-login.jsp', 
	'admin/login.js', 'sign_in/', 'admin.htm', 'check.jsp', 
	'administrators/', 'usuarios/login.js', 'admin/cp.html', 
	'check.js', 'log-in.jsp', 'uvpanel/', 'cgi-bin/loginjs', 
	'letmein/', 'sysadmin.jsp', 'sign-in.jsp', 'simpleLogin/', 
	'administrator/login.js', 'member/', 'super_indexjs', 
	'admin/cp.js', 'moderator/login.jsp', 'cmsadmin/', 
	'checkadmin.js', 'bb-admin/index.html', 'adminlogin.js', 
	'nsw/admin/login.jsp', 'UserLogin/', 'webadmin/admin.js', 
	'admin_login.html', 'admin2.jsp', 'adminarea/login.html', 
	'administrator/index.js', 'cmsadmin.jsp', 'users.jsp', 
	'webadmin/login.jsp', 'login_userjs', 'loginsuperjs', 
	'LiveUser_Admin/', 'staradmin/', 'adminarea/admin.js', 
	'modelsearch/admin.jsp', 'loginok/', 'panel/', 
	'Lotus_Domino_Admin/', 'admin/index.js', 'admincontrol.html', 
	'webadmin/admin.html', 'panel-administracion/login.js', 
	'administration.jsp', 'login/', 'myadmin/', 'webadmin/index.jsp',
	'adminitem/', 'admin2/', 'superjs', 'admin/admin-login.js', 
	'sysadm.js', 'super_loginjsp', 'isadmin.jsp', 'logoutjsp', 
	'administratie/', 'login1js', 'processlogin.jsp', 
	'modelsearch/admin.js', 'adminLogin.js', 'usuarios/login.jsp', 
	'superman/', 'admin/account.jsp', 'secret/', 'signin.js', 
	'modules/admin/', 'bb-admin/admin.html', 'adminitems.js', 
	'adminitem.js', 'admin1.jsp', 'admincontrol/', 'super1jsp', 
	'phpldapadmin/', 'utility_login/', 'meta_login/', 'login_outjsp',
	'adm/index.jsp', 'management/', 'bbadmin/', 'security/', 
	'authentication.jsp', 'user.jsp', 'superuser.js', 'log-in.js', 
	'openvpnadmin/', 'panel.jsp', 'moderator.jsp', 'moderator/', 
	'ServerAdministrator/', 'super1/', 'kpanel/', 'administrivia/', 
	'webadmin.jsp', 'cpanel_file/', 'administrator/login.html', 
	'admin5/', 'siteadmin/', 'supermanjs', 'Super-Admin/', 
	'admincp/index.html', 'manage/', 'webmaster.jsp', 
	'siteadmin/login.jsp', 'signin/', 
	'panel-administracion/index.jsp', 'blog/wp-login.jsp', 
	'admin/login.jsp', 'AdminTools/', 'authenticate.jsp', 
	'admin1.htm', 'wp-login.js', 'administrators.js', 'sign_in.jsp', 
	'administratorlogin/', 'pages/admin/', 'adminLogin/', 'adm.jsp', 
	'webadmin/', 'instadmin/', 'account.jsp', 'login_userjsp', 
	'administratorlogin.js', 'server_admin_small/', 'loginsave/', 
	'manuallogin/', 'adminarea/', 'cp.js', 'typo3/', 'signin.jsp', 
	'controlpanel.js', 'panel-administracion/login.jsp', 'login-us/',
	'siteadmin/index.js', 'admin/home.jsp', 'adminarea/login.jsp', 
	'administrator/index.html', 'webadmin/admin.jsp', 
	'admin_area/index.jsp', 'modelsearch/admin.html', 'wp-login.jsp',
	'admin2.html', 'autologin.jsp', 'logo_sysadmin/', 
	'login_adminjsp', 'login_out/', 'access.jsp', 'autologin/', 
	'webadmin/login.html', 'sysadm/', 'yonetim.html', 
	'admin-login.jsp', 'admin.jsp', 'affiliate.jsp', 'Server/', 
	'user/admin.js', 'loginerror/', 'usuario/', 'hpwebjetadmin/', 
	'blogindex/', 'users/admin.js', 'adminpanel/', 'adm/index.js', 
	'adm.html', 'adm/', 'admin_area/admin.html', 'banneradmin/', 
	'adm.js', 'SysAdmin2/', 'superjsp', 'auth.jsp', 'Server.jsp', 
	'yonetici.jsp', 'member.js', 'pages/admin/admin-login.jsp', 
	'navSiteAdmin/', 'admin/', 'administr8/', 'admin/index.html', 
	'sysadmin.js', 'wizmysqladmin/', 'sys-admin/', 
	'admin/controlpanel.js', 'logoutjs', 'adminpro/', 
	'admin/account.html', 'management.jsp', 'vmailadmin/', 
	'sshadmin/', 'panel-administracion/admin.jsp', 
	'panel-administracion/login.html', 'admin/admin_login.js', 
	'admin/admin.jsp', 'adminarea/admin.html', 'manager.js', 
	'admin3/', 'cgi-bin/loginjsp', 'administrator/account.jsp', 
	'webadmin/index.js', 'authadmin.js', 'ezsqliteadmin/', 
	'useradmin/', 'members.jsp', 'admin2/login.js', 
	'siteadmin/index.jsp', 'administrator.html', 'checkuser.jsp', 
	'wp-admin/', 'rcLogin/', 'fileadmin.jsp', 'superuser.jsp', 
	'login_adminjs', 'admin/cp.jsp', 'checkadmin.jsp', 'newsadmin/', 
	'authuser.jsp', 'manage.js', 'home.html', 'globes_admin/', 
	'fileadmin/', 'administr8.jsp', 'admin_area/login.js', 
	'sql-admin/', 'manager/', 'panel-administracion/admin.html', 
	'acceso.jsp', 'moderator/login.html', 'log_in.jsp', 'ur-admin.js'
	, 'modelsearch/index.jsp', 'members.js', 'adminarea/index.jsp', 
	'bb-admin/', 'relogin.jsp', 'supervise/', 'yonetici.js', 
	'login_db/', 'login1/', 'account.js', 'authentication.js', 
	'login-redirect/', '0manager/', 'blog/wp-login.js', 
	'administrator/account.js', 'admin/adminLogin.jsp', 
	'moderator.php', 'admin2/index.js', 'vorod.jsp', 'management.js',
	'adminpanel.html', 'sub-login/', 'sign_in.js', 'yonetim.js', 
	'admin_area/login.html', 'access/', 'adminarea/index.html', 
	'SysAdmin/', 'wp-login/', 'relogin.js', 'yonetim.jsp', 
	'admincp/login.asp', 'admin/controlpanel.jsp', 
	'administratorlogin.jsp', 'cadmins/', 'adminsite/', 'power_user/'
	, 'admin/login.html', 'admin/admin.js', 'superuserjs', 
	'memberadmin/', 'supermanjsp', 'admincp/', 
	'administrator/index.jsp', 'moderator/admin.jsp', 
	'moderator/admin.js', 'xlogin/', 'registration/', 
	'memberadmin.jsp', 'adminpanel.js', 'controlpanel.jsp', 
	'admincontrol.jsp', 'cmsadmin.js', 'ss_vms_admin_sm/', 
	'rcjakar/admin/login.jsp', 'letmein.js', 'admins.jsp', 
	'webadmin.js', 'vadmind/', 'adminLogin.html', 'login.js', 
	'adm_auth.js', 'login.html', 'admin4_account/', 'cp.jsp', 
	'system_administration/', 'pages/admin/admin-login.js', 
	'bb-admin/index.jsp', 'webadmin/login.js', 'accounts.js', 
	'admin_area.jsp', 'admin2.js', 'adminLogin.jsp', 
	'administrator/account.html', 'supervise/Loginjsp', 'administer/'
	, 'Database_Administration/', 'ur-admin/', 'admin_area/admin.js',
	'bb-admin/login.html', 'users/', 'moderator.html', 
	'super_loginjs', 'login.htm', 'Server.js', 'controlpanel/', 
	'siteadmin.jsp', 'accounts.jsp', 'relogin.html', 'phppgadmin/', 
	'moderator.js', 'admin1.html', 'webmaster.js', 'loginflat/', 
	'admin/account.js', 'macadmin/', 'logout/', 'formslogin/', 
	'supermanagerjsp', 'login.jsp', 'home.js', 'vorud.jsp', 
	'manage.jsp', 'log_in.js', 'dir-login/', 'wp-login.php', 
	'control/', 'siteadmin.js', 'bb-admin/admin.js', 
	'modelsearch/login.js', 'administrator.js', 'panel.js', 
	'acceso.js', 'root/', 'adminitem.jsp', 'admincontrol/login.jsp', 
	'login1jsp', 'yonetici.html', 'usuarios/', 'admin/index.jsp', 
	'secrets/', 'rcjakar/admin/login.js', 'administrator/login.jsp', 
	'ccp14admin/', 'moderator/admin.html', 'bb-admin/login.js', 
	'modelsearch/index.html', 'fileadmin.js', 'relogin.htm', 
	'adminitems.jsp', 'usr/', 'isadmin.js', 'login_outjs', 
	'project-admins/', 'checklogin.js', 'admincp/login.jsp', 
	'modelsearch/login.jsp', 'bb-admin/login.jsp', 'admins/', 
	'radmind/', 'user/', 'admin-login.js', 'webadmin/index.html', 
	'log-in/', 'vorud/', 'panel-administracion/', 'admincontrol.js', 
	'super1js', 'administration.js', 'admin/adminLogin.htm', 
	'moderator/login.js', 'admin_login.js', 'adminlogin.jsp', 
	'adminarea/admin.jsp', 'members/', 'vorod/', 'user.html', 
	'nsw/admin/login.js', 'admincp/login.js', 'admin/admin.html', 
	'bb-admin/index.js', 'cpanel/', 'loginsuperjsp'
	]

    others = [
	'Lotus_Domino_Admin/', 'admin_area/login.html', 
	'admin/adminLogin.cgi', 'siteadmin/login.html', 
	'panel-administracion/login.brf', 'Database_Administration/', 
	'adminpanel.cgi', 'adminLogin.cfm', 'siteadmin/login.cfm', 
	'project-admins/', 'aadmin/', 'admins.cgi', 'sysadmin.brf', 
	'admins/', 'admin2/login.cfm', 'admin_area/login.cgi', 
	'webadmin/admin.brf', 'yonetici.html', 'adm.brf', 'admin.cfm', 
	'admin_area.cgi', 'adminarea/index.brf', 'checkadmin.brf', 
	'vorod/', 'log-in/', 'admin2/index.brf', 'panel-administracion/',
	'admin/admin.html', 'administration.brf', 'sign-in.cgi', 
	'modelsearch/login.cfm', 'moderator.cgi', 
	'modelsearch/login.html', 'administrator/login.cfm', 
	'affiliate.cgi', 'processlogin.brf', 'sub-login/', 
	'autologin.cgi', 'administr8.cgi', 'modelsearch/index.html', 
	'login.brf', 'admin.brf', 'moderator/', 'usuarios/login.brf', 
	'adm.cgi', 'admin1.htm', 'webmaster/', 'account.brf', 
	'adm_auth.cgi', 'superuser/', 'supermanagercgi', 'adm_auth.cfm', 
	'wizmysqladmin/', 'admin_area/admin.brf', 'user.brf', 
	'log_in.brf', 'bigadmin/', 'sysadm.brf', 'acct_login/', 
	'admin-login.html', 'signin/', 'administratie/', 
	'administratorlogin/', 'admincp/login.cgi', 'moderator.cfm', 
	'usr/', 'SysAdmin/', 'administratorlogin.brf', 'home.brf', 
	'adm/index.cfm', 'cpanel_file/', 'login.cfm', 
	'adm/admloginuser.cfm', 'vorod.brf', 'controlpanel.brf', 
	'SysAdmin2/', '0manager/', 'webmaster.cgi', 'administrators/', 
	'admin/adminLogin.html', 'administrator/index.html', 
	'controlpanel/', 'adminLogin.brf', 'control.cgi', 
	'moderator/admin.html', 'check.cgi', 'phpSQLiteAdmin/', 
	'admin/controlpanel.htm', 'signin.brf', 'admin_area/login.brf', 
	'radmind/', 'administrators.cgi', 'acceso.cfm', 'sign_in/', 
	'webmaster.brf', 'cgi-bin/logincgi', 'admin/account.cgi', 
	'user.cgi', 'modelsearch/admin.brf', 'loginsuper/', 
	'adminlogin.cgi', 'supercgi', 'login_adminbrf', 'banneradmin/', 
	'modelsearch/index.brf', 'hpwebjetadmin/', 'admin4_colon/', 
	'affiliate.brf', 'authuser.brf', 'adminarea/login.html', 
	'sysadm.cgi', 'webadmin/index.html', 'admin_area/admin.cgi', 
	'admin/admin_login.cfm', 'members/', 'globes_admin/', 
	'cmsadmin.cgi', 'admin/cp.html', 'controlpanel.cgi', 
	'authadmin.cgi', 'admin/admin-login.cgi', 'super1/', 
	'accounts.cgi', 'admincontrol/', 'cpanel/', 'phppgadmin/', 
	'login_usercgi', 'admincp/', 'logincgi', 'bb-admin/index.cfm', 
	'vmailadmin/', 'log_in.cgi', 'panel-administracion/index.html', 
	'uvpanel/', 'adminpanel.brf', 'admin/admin_login.html', 
	'webadmin/admin.html', 'smblogin/', 'supervise/', 'login_admin/',
	'webadmin/index.brf', 'UserLogin/', 'super1brf', 
	'authentication.brf', 'bb-admin/admin.cfm', 'nsw/admin/login.cfm'
	, 'admin/login.html', 'superuser.brf', 'auth.brf', 
	'administratorlogin.cgi', 'webadmin/admin.cfm', 'control/', 
	'users/admin.brf', 'siteadmin/index.cfm', 'admin/home.cgi', 
	'user/admin.cgi', 'accounts.brf', 'Server/', 'adminpanel.cfm', 
	'ur-admin.brf', 'auth.cgi', 'admin1.brf', 'yonetim.cgi', 
	'super_indexbrf', 'memlogin/', 'login.htm', 'ezsqliteadmin/', 
	'superuserbrf', 'supermancgi', 'authadmin.brf', 
	'admin/controlpanel.cgi', 'showlogin/', 'adm_auth.brf', 
	'Indy_admin/', 'admincontrol.html', 'openvpnadmin/', 'vorud/', 
	'relogin.brf', 'isadmin.cgi', 'access/', 'registration/', 
	'admin4/', 'cmsadmin/', 'webadmin.brf', 'admincontrol/login.cfm',
	'pgadmin/', 'admin/index.html', 'admin-login.brf', 'ur-admin/', 
	'relogin.cgi', 'cp.brf', 'blog/wp-login.brf', 
	'moderator/login.html', 'adm.html', 'controlpanel.cfm', 
	'loginbrf', 'admin/admin-login.cfm', 'administrator/index.cfm', 
	'adminsite/', 'manage.cgi', 'relogin.htm', 'admin1.html', 
	'adminarea/admin.brf', 'home.cfm', 'admin/admin.cgi', 'super1cgi'
	, 'administration/', 'admin/admin-login.brf', 'home.html', 
	'supervise/Loginbrf', 'modelsearch/index.cfm', 'manuallogin/', 
	'sign_in.brf', 'admin/cp.cfm', 'memberadmin/', 'adminLogin.html',
	'login_outbrf', 'admin/adminLogin.htm', 'ccp14admin/', 
	'modules/admin/', 'admincontrol/login.html', 'newsadmin/', 
	'administrator.cfm', 'modelsearch/admin.cfm', 'administr8/', 
	'checkuser.cgi', 'panel-administracion/login.cfm', 'bbadmin/', 
	'secrets/', 'admin/home.brf', 'webadmin/login.cfm', 
	'yonetici.cgi', 'adminarea/admin.cfm', 'power_user/', 
	'administrator/login.html', 'secret/', 'admin_area/login.cfm', 
	'manager/', 'sysadmin.cgi', 'myadmin/', 'wp-login.cfm', 'cp.cgi',
	'panel/', 'admin_area.brf', 'vorud.cgi', 'adminLogin/', 
	'bb-admin/login.brf', 'admin/controlpanel.html', 'sys-admin/', 
	'macadmin/', 'super_indexcgi', 'user/', 'admin-login.cgi', 
	'bb-admin/admin.html', 'moderator/login.cgi', 
	'modelsearch/login.brf', 'memberadmin.cgi', 'access.brf', 
	'instadmin/', 'security/', 'affiliate.cfm', 'admin.htm', 'typo3/'
	, 'server_admin_small/', 'super_loginbrf', 'isadmin.brf', 
	'Super-Admin/', 'admloginuser.cfm', 'cp.html', 'admin2.cgi', 
	'adminarea/login.brf', 'admin_area/admin.cfm', 'panel.cgi', 
	'user.cfm', 'administrator/index.brf', 'login_userbrf', 
	'administrator/account.brf', 'webadmin/login.html', 'logout/', 
	'adm/', 'panel-administracion/admin.cfm', 'admin/cp.brf', 
	'navSiteAdmin/', 'platz_login/', 'admin/admin_login.brf', 
	'LiveUser_Admin/', 'yonetim.html', 'manager.cgi', 'vadmind/', 
	'checklogin.brf', 'dir-login/', 'pages/admin/admin-login.cfm', 
	'administrator/login.brf', 'directadmin/', 'adminpro/', 
	'staradmin/', 'admin_area/admin.html', 'admin/admin.brf', 
	'superuser.cgi', 'utility_login/', 'login/', 'adm/index.html', 
	'bb-admin/admin.cgi', 'phpldapadmin/', 'bb-admin/login.cfm', 
	'admin/login.cgi', 'manage/', 'rcjakar/admin/login.cfm', 
	'modelsearch/admin.html', 'sql-admin/', 'supermanbrf', 'admin5/',
	'usuario/', 'moderator.html', 'admin_area/', 'acceso.cgi', 
	'irc-macadmin/', 'bb-admin/admin.brf', 'rcjakar/admin/login.brf',
	'admin/account.cfm', 'letmein.brf', 'adminitem.brf', 
	'administr8.brf', 'adminarea/index.cfm', 'meta_login/', 
	'adminitems/', 'webadmin/', 'pureadmin/', 
	'admin/controlpanel.cfm', 'admincp/index.html', 'webadmin.html', 
	'wp-login/', 'fileadmin.cgi', 'admin_login.cgi', 'Server.cgi', 
	'sign-in.brf', 'root/', 'panel-administracion/index.brf', 
	'bb-admin/index.brf', 'fileadmin.brf', 'adminitems.cgi', 
	'administrator.brf', 'simpleLogin/', 'loginerror/', 
	'admincontrol.brf', 'moderator.brf', 'access.cgi', 'logoutbrf', 
	'superman/', 'panel-administracion/login.html', 
	'moderator/login.brf', 'signin.cgi', 'sysadm/', 'member.cgi', 
	'moderator/admin.cgi', 'usuarios/', 'admincontrol.cfm', 
	'logo_sysadmin/', 'admin_area/index.cfm', 'admin2.cfm', 
	'letmein.cgi', 'autologin/', 'administrator/login.cgi', 
	'adminarea/login.cfm', 'AdminTools/', 'members.cgi', 'admin2/', 
	'supervise/Logincgi', 'login_outcgi', 
	'pages/admin/admin-login.brf', 'admin/cp.cgi', 'loginsave/', 
	'member/', 'logoutcgi', 'manager.brf', 'fileadmin/', 'check.brf',
	'pages/admin/', 'account.cfm', 'adm.cfm', 
	'system-administration/', 'management/', 'nsw/admin/login.brf', 
	'administratorlogin.cfm', 'admin/admin.cfm', 'user.html', 
	'admin/', 'administrator/', 'accounts/', 'login_db/', 
	'admin/home.cfm', 'webadmin.cgi', 'manage.brf', 'log-in.brf', 
	'admin/account.html', 'admin/index.cfm', 'user/admin.brf', 
	'adminitem/', 'wp-login.php', 'admin/login.brf', 
	'administrator/account.cgi', 'system_administration/', 
	'loginflat/', 'login-redirect/', 'loginok/', 'log-in.cgi', 
	'loginsuperbrf', 'ur-admin.cgi', 'login_out/', 
	'panel-administracion/admin.brf', 'admin2/index.cfm', 'vorod.cgi'
	, 'kpanel/', 'admin_login.brf', 'cp.cfm', 'useradmin/', 
	'admin-login.cfm', 'moderator/login.cfm', 'management.cgi', 
	'administrivia/', 'ServerAdministrator/', 'memberadmin.cfm', 
	'users/', 'login.html', 'authenticate.cgi', 
	'administrator/account.html', 'Server.brf', 'sign_in.cgi', 
	'admloginuser.brf', 'yonetim.brf', 'log_in/', 'admin/home.html', 
	'wp-login.brf', 'admin.cgi', 'admin_login.cfm', 'formslogin/', 
	'memberadmin.brf', 'userlogin.brf', 'administration.cgi', 
	'admin/admin-login.html', 'admin2/login.brf', 'moderator.php', 
	'administer/', 'administrator.html', 'bb-admin/index.html', 
	'loginsupercgi', 'modelsearch/login.cgi', 'blogindex/', 
	'rcLogin/', 'users.brf', 'siteadmin/login.brf', 
	'authentication.cgi', 'authuser.cgi', 'authenticate.brf', 
	'control.brf', 'adminitems.brf', 'autologin.brf', 'admin1.cgi', 
	'admin.html', 'adminpanel.html', 'acceso.brf', 'secure/', 
	'sshadmin/', 'bb-admin/', 'admin/index.brf', 
	'pages/admin/admin-login.cgi', 'adminarea/index.html', 
	'adminarea/', 'login-us/', 'userlogin.cgi', 'users/admin.cgi', 
	'cadmins/', 'checkuser.brf', 'adminpanel/', 'PSUser/', 
	'administratoraccounts/', 'cgi-bin/loginbrf', 'users.cgi', 
	'adminitem.cgi', 'supermanagerbrf', 'usuarios/login.cfm', 
	'webadmin/login.brfbrf', 'admin/admin_login.cgi', 'wp-admin/', 
	'login1cgi', 'super_logincgi', 'admin/adminLogin.cfm', 
	'yonetici.brf', 'member.brf', 'panel.brf', 'adminarea/admin.html'
	, 'login1brf', 'siteadmin.brf', 'adm/index.brf', 
	'admin_login.html', 'admin3/', 'vorud.brf', 
	'panel-administracion/admin.html', 'controlpanel.html', 
	'customer_login/', 'management.brf', 'admin2.brf', 
	'panel-administracion/login.cgi', 'checklogin.cgi', 
	'admin_area/index.brf', 'siteadmin/', 'admincp/login.brf', 
	'admin1/', 'admin2.html', 'admin_area/index.html', 
	'checkadmin.cgi', 'pages/admin/admin-login.html', 'letmein/', 
	'admin/controlpanel.brf', 'superusercgi', 'cmsadmin.brf', 
	'supervisor/', 'login1/', 'adminlogin.brf', 'account.html', 
	'sysadmins/', 'ss_vms_admin_sm/', 'moderator/admin.brf', 
	'moderator/admin.cfm', 'admincontrol.cgi', 'members.brf', 
	'admin/login.htm', 'radmind-1/', 'bb-admin/login.html', 
	'login_admincgi', 'processlogin.cgi', 'administrator.cgi', 
	'admin/login.cfm', 'bb-admin/login.cgi', 'admins.brf', 
	'admin/account.brf', 'admin4_account/', 
	'panel-administracion/index.cfm', 'login.cgi', 
	'admincontrol/login.brf', 'webadmin.cfm', 'relogin.html', 
	'blog/wp-login.cgi', 'admin/adminLogin.brf', 
	'adm/admloginuser.brf', 'webadmin/index.cfm', 'support_login/', 
	'administrator/account.cfm', 'superbrf', '0admin/', 'sign-in/', 
	'xlogin/', 'siteadmin.cgi', 'cp/', 'siteadmin/index.brf', 
	'administrators.brf'
	]    

    noidea = php+asp+jsp+others
    found=0
    def urlFetch(getOption, SSLOption, getPath, getNetloc, getPort):
        mf.writelines("The administrative login page is found at: \n")
        found=0
        for urn in getOption:
                urn = getPath + "/" + urn
                uri = getNetloc+urn
                print ("\t >> Testing " + uri +" - Port: " +str(getPort))
                if SSLOption == "1":
                    link = httplib.HTTPConnection(getNetloc, getPort)
                else:
                    link = httplib.HTTPSConnection(getNetloc, getPort)
                link.request("GET",urn, headers={ 'User-Agent': 'Mozilla/5.0' })
                reply = link.getresponse()
                if reply.status != 200:
                    found=found
                    
                else:
                    found=found+1
                    print "\t", uri, "***FOUND*** \n" 
                    print "##### The administration page is available at ", uri, "##### \n"
                    mf.writelines(uri+"\n")
        print("\nScan has been completed\n")
        print "<< Found",found,"admin pages >>"
        return found

    try:
        url = raw_input("Enter the URL to be scanned: ")
        regex = re.compile(
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' # domain...
            r'localhost|' # localhost...
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|' # ...or ipv4
            r'\[?[A-F0-9]*:[A-F0-9:]+\]?)' # ...or ipv6
            r'(?::\d+)?' # optional port
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)
        validate = regex.match(url)
        if validate == None:
            print "\n<< Wrong URL input! >>\n"
            exit()

        url="//"+url
        url=urlparse.urlparse(url)
        if url.port:
            getPort= url.port
        else:
            getPort=80;
        getPath= url.path
        getNetloc= url.netloc
        getNetloc= getNetloc.replace(":","")
        getNetloc= getNetloc.replace(str(getPort),"")
                
        mf=open(getNetloc+getPath.replace("/","-")+"_port_"+str(getPort)+".txt",'w')
        print "Choose the type of the website:"
        print "1. ASP"
        print "2. JSP"
        print "3. PHP"
        print "4. Others"
        print "0. IDK (Searches all types - takes longer time)"
        print "\nFor example, enter 1 if it is a ASP site, 2 for JSP, 3 for PHP and 4 for others"

        option=raw_input("Enter your choice -> ")
        if option != "1" or option != "2" or option != "3" or option != "4":
            option = "0"

        print "\nSSL Support option:\n"
        print "1. SSL disabled (HTTP)"
        print "2. SSL enabled (HTTPS)"
        print "\nEnter 1 to disable SSL, enter 2 to enable SSL"         
        SSLOption=raw_input("Enter your choice ->")
        if SSLOption != "2":
            SSLOption = "1"
        
        if SSLOption == "2" and getPort==80:
           getPort = 443

        if option=='1':
            found=urlFetch(asp, SSLOption, getPath, getNetloc, getPort)

        if option=='2':
            found=urlFetch(jsp, SSLOption, getPath, getNetloc, getPort)

        if option=='3':
            found=urlFetch(php, SSLOption, getPath, getNetloc, getPort)           

        if option=='4':
            found=urlFetch(others, SSLOption, getPath, getNetloc, getPort)

        if option=='0':
            found=urlFetch(noidea, SSLOption, getPath, getNetloc, getPort)

        if found==0:
            mf=open(getNetloc+getPath.replace("/","-")+"_port_"+str(getPort)+".txt",'a')
            mf.writelines("No administrative login page was found :( \n")
            mf.close()
        
        print "\nRobots file status:"
        link = httplib.HTTPConnection(getNetloc, getPort)
        link.request("GET","/robots.txt", headers={ 'User-Agent': 'Mozilla/5.0' })
        reply = link.getresponse()
        if reply.status == 404:
            print "No robots.txt file found!"
            mf=open(getNetloc+getPath.replace("/","-")+"_port_"+str(getPort)+".txt",'a')
            mf.writelines("Robots file status:\n")
            mf.writelines("No robots.txt file found!")
            mf.close()
        else:
            print "The robots.txt file is available at: "+getNetloc+"/robots.txt\nTake a look!"
            mf=open(getNetloc+getPath.replace("/","-")+"_port_"+str(getPort)+".txt",'a')
            mf.writelines("Robots file status:\n")
            mf.writelines("The robots.txt file is available at: "+getNetloc+"/robots.txt")
            mf.close()           

        print("\nLog file for this scan has been created at "+os.getcwd()+"\n")

    except (httplib.HTTPResponse, socket.error) as Exit:
        print("\nPlease enter a valid URL and port. Example:")
        print("1. www.example.com")
        print("2. www.example.com:443")
        print("3. www.example.com:8080/path")
        print("\nOr try to change SSL Support Option\n")
        mf.close()
        if os.path.isfile(getNetloc+getPath.replace("/","-")+"_port_"+str(getPort)+'.txt'):
            os.remove(getNetloc+getPath.replace("/","-")+"_port_"+str(getPort)+'.txt')
        exit()

except (httplib.HTTPResponse, socket.error):
    print "Check your Internet connection or firewall settings "
