# devlabs

## Repository for devops course

1. Створив порожній репозиторій на Github, створив однойменний каталог на локальній машині, ввів в консолі наступні команди.

	```console
	vasyl@vasyl-HP-Laptop-15-bs0xx:~/devlabs$ echo "# devlabs" >> README.md
	vasyl@vasyl-HP-Laptop-15-bs0xx:~/devlabs$ git init
	Initialized empty Git repository in /home/vasyl/devlabs/.git/
	vasyl@vasyl-HP-Laptop-15-bs0xx:~/devlabs$ git add README.md
	vasyl@vasyl-HP-Laptop-15-bs0xx:~/devlabs$ git commit -m "lab1: first commit"
	[master (root-commit) cc014b8] lab1: first commit
	1 file changed, 1 insertion(+)
	create mode 100644 README.md
	vasyl@vasyl-HP-Laptop-15-bs0xx:~/devlabs$ git remote add origin https://github.com/vkrenta/devlabs.git
	vasyl@vasyl-HP-Laptop-15-bs0xx:~/devlabs$ git push -u origin master
	```
	
1. Таким чином я створив файл **README.md**, ініціював порожній репозиторій, додав файл до репозиторію, створив перший коміт, синхронізував репозиторій з Github, зберіг зміни на сервері.
1. Ввів дану команду і отримав хеш першого коміту

	```console
	vasyl@vasyl-HP-Laptop-15-bs0xx:~/devlabs$ git log
	commit cc014b81d6546a5103d650b6fcb9f70683368969 (HEAD -> master, origin/master)
	Author: vkrenta <52718389+vkrenta@users.noreply.github.com>
	Date:   Thu Oct 10 17:32:24 2019 +0300

		lab1: first commit
	```

1. Створив гілку, перейшов на неї, зробив зміни у файлі, однак вони на першій гілці не відображаються, оскільки запушені на другій.
1. З допомогою команди **git checkout -b second_branch** створив нову гілку і переключився на неї.
