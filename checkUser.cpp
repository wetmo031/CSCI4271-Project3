// current function
bool RegDB::checkUserSQL(const std::string &user) {
    string cmd = "python3 " + dbPath + "/checkUser.py " + user;
    return (system(cmd.c_str()) == 0);
}

// updated function
bool RegDB::checkUserSQL(const std::string &user) {
   pid_t pid = fork();
   if (pid == 0) {
       execl("/usr/bin/python3", "python3", (dbPath + "/checkUser.py").c_str(), user.c_str(), (char *)NULL);
       exit(EXIT_FAILURE);  
   } else if (pid < 0) {
       return false;
   } else {
       int status;
       waitpid(pid, &status, 0);
       return WIFEXITED(status) && WEXITSTATUS(status) == 0;
   }
}
