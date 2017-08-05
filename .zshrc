ZSH=$HOME/Applications/oh-my-zsh
# Set name of the theme to load.
# Look in ~/.oh-my-zsh/themes/
# Optionally, if you set this to "random", it'll load a random theme each
# time that oh-my-zsh is loaded.
ZSH_THEME="ys"

# Uncomment the following line to use case-sensitive completion.
# CASE_SENSITIVE="true"

# Uncomment the following line to disable bi-weekly auto-update checks.
# DISABLE_AUTO_UPDATE="true"

# Uncomment the following line to change how often to auto-update (in days).
# export UPDATE_ZSH_DAYS=13

# Uncomment the following line to disable colors in ls.
# DISABLE_LS_COLORS="true"

# Uncomment the following line to disable auto-setting terminal title.
# DISABLE_AUTO_TITLE="true"

# Uncomment the following line to enable command auto-correction.
# ENABLE_CORRECTION="true"

# Uncomment the following line to display red dots whilst waiting for completion.
# COMPLETION_WAITING_DOTS="true"

# Uncomment the following line if you want to disable marking untracked files
# under VCS as dirty. This makes repository status check for large repositories
# much, much faster.
# DISABLE_UNTRACKED_FILES_DIRTY="true"

# Uncomment the following line if you want to change the command execution time
# stamp shown in the history command output.
# The optional three formats: "mm/dd/yyyy"|"dd.mm.yyyy"|"yyyy-mm-dd"
# HIST_STAMPS="mm/dd/yyyy"

# Would you like to use another custom folder than $ZSH/custom?
# ZSH_CUSTOM=/path/to/new-custom-folder

# Which plugins would you like to load? (plugins can be found in ~/.oh-my-zsh/plugins/*)
# Custom plugins may be added to ~/.oh-my-zsh/custom/plugins/
# Example format: plugins=(rails git textmate ruby lighthouse)
# Add wisely, as too many plugins slow down shell startup.
plugins=(git d ls copydir web-search)

source $ZSH/oh-my-zsh.sh

# User configuration
alias vim='/Applications/MacVim.App/Contents/MacOS/Vim'
alias vi='/Applications/MacVim.App/Contents/MacOS/Vim'
alias py='/usr/bin/python'

export PATH=/Users/zhenhaiyu/anaconda/bin:/usr/local/bin:$HOME/bin:$PATH
# export PYTHONPATH=/usr/local/lib/python2.7/site-packages/
function javagen()
{
    cp ~/Documents/Templates/Solution.java ./$1.java
    subl ./$1.java
}

function solu()
{
    mkdir $1
    cd $1
    echo "===" > README.md
    cp ~/Documents/Templates/Solution.java . 
    subl .
}

function javamake()
{
    javac $1.java && java $1
    rm $1.class
}

function cppgen()
{
    cp ~/Documents/Templates/cpp_template.cpp ./$1.cpp
    vim ./$1.cpp
}

function cppmake()
{
    g++ ./$1.cpp -o $1
    echo "done compiling"
    ./$1
}

function pygen()
{
    cp ~/Documents/Templates/py_template.py ./$1.py
    vim ./$1.py
}

function htmlgen()
{
    cp ~/Documents/Templates/main.html .
    vim ./main.html
}

alias sshcs="ssh h2zhen@linux.student.cs.uwaterloo.ca"
alias cdrepo="cd /Users/zhenhaiyu/Documents/Git_Repo"
alias cdmooc="cd /Users/zhenhaiyu/Documents/MOOC"

alias gits="git status"
alias gitps="git push"
alias gitpl="git pull"
alias gitc="git commit"
alias gob="go build"
alias gor="go run"

function gita()
{
    git add $1
}

alias ctag="ctags -R --fields=+l ."
# export MANPATH="/usr/local/man:$MANPATH"

# You may need to manually set your language environment
# export LANG=en_US.UTF-8

# Preferred editor for local and remote sessions
# if [[ -n $SSH_CONNECTION ]]; then
#   export EDITOR='vim'
# else
#   export EDITOR='mvim'
# fi

# Compilation flags
# export ARCHFLAGS="-arch x86_64"

# ssh
# export SSH_KEY_PATH="~/.ssh/dsa_id"

# Set personal aliases, overriding those provided by oh-my-zsh libs,
# plugins, and themes. Aliases can be placed here, though oh-my-zsh
# users are encouraged to define aliases within the ZSH_CUSTOM folder.
# For a full list of active aliases, run `alias`.
#
# Example aliases
# alias zshconfig="mate ~/.zshrc"
# alias ohmyzsh="mate ~/.oh-my-zsh"
eval "$(rbenv init -)"

test -e "${HOME}/.iterm2_shell_integration.zsh" && source "${HOME}/.iterm2_shell_integration.zsh"

