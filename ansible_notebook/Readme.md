file
	在目标主机创建文件或目录，并赋予其系统权限
	- name: create a file
  file: 'path=/root/foo.txt state=touch mode=0755 owner=foo group=foo'
copy
	实现Ansible服务端到目标主机的文件传送
	- name: copy a file
  copy: 'remote_src=no src=roles/testbox/files/foo.sh dest=/root/foo.sh mode=0644 force=yes'
stat
	获取远程文件状态信息
	- name: check if foo.sh exists
   stat: 'path=/root/foo.sh'
   register:script_stat
debug
	打印语句到ansible执行输出
	- debug: msg=foo.sh exists
   when: script_stat.stat.exists
command/shell
	用来执行Linux目标主机命令行
	- name: run the script
   command: "sh /root/foo.sh"
		command不能调用系统变量
	- name: run the script
   shell: "echo 'test' > /root/test.txt"
		shell模式可以调用系统变量
template
	实现ansible服务端到目标主机的jinja2模板传送
	- name: write the nginx config file
   template: src=roles/testbox/templates/nginx.conf.j2 dest=/etc/nginx/nginx.conf
packaging
	调用目标主机系统包管理工具(yum,apt)进行安装
	- name: ensure nginx is at the latest version
   yum: pkg=nginx state=latest
		Centos/Redhat系统
service
	管理目标主机系统服务
	- name: start nginx service
   service: name=nginx state=started