
### Github

```bash
cd path/to/your/repo
git status
git add .
git commit -m "Your commit message"
git pull origin your-branch-name
git push origin your-branch-name
```

### CMD

-   `ls`: List contents of the current directory.
-   `cd`: Change the current directory.
-   `pwd`: Print the current working directory.
-   `mkdir`: Create a new directory.
-   `touch`: Create a new file.
-   `cp`: Copy files or directories.
-   `mv`: Move or rename files or directories.
-   `rm`: Remove files or directories.
-   `sudo`: Run a command with superuser (root) privileges.
-   `top`: Show a list of processes and their system resource usage.
-   `kill`: Terminate a process by ID or name.
-   `man`: Display the manual page for a command.
-   `history`: Show a list of recently executed commands.
-   `grep`: Search for a pattern in a file or output of a command.
-   `chmod`: Change file permissions.
-   `chown`: Change file owner and group.
-   `df`: Show disk space usage.
-   `du`: Show disk usage for a file or directory.
-   `find`: Search for files or directories that match certain criteria.
-   `tar`: Create or extract compressed archive files.
-   `ssh`: Connect to a remote system using SSH.
-   `scp`: Copy files securely between systems using SSH.
-   `rsync`: Synchronize files and directories between systems.
-   `curl`: Transfer data from or to a server using various protocols.
-   `wget`: Download files from the internet.
-   `ping`: Test connectivity to a network host.
-   `traceroute`: Show the path packets take to reach a network host.

```bash 
touch Filename
```

Run Container

```bash

docker run -d --name app -p 5000:5000 -p 8501:8501 -p 8888:8888 app
```

Get rid of all old containers

```bash

docker container prune

```

[Jupyter](http://localhost:8888/lab)
