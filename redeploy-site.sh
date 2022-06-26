#! /bin/bash

cd /root/project-kds_danieldiaz
git fetch && git reset origin/main --hard
python -m venv python3-virtualenv
source python3-virtualenv/bin/activate
pip install -r requirements.txt
systemctl restart myportfolio

#session="portfolio_ddl29"
#tmux new-session -d -s $session -c /root/project-kds_danieldiaz
#window=0
#tmux rename-window -t $session:$window 'portddl29'
#tmux send-keys -t $session:$window 'git fetch && git reset origin/main --hard' C-m
#tmux send-keys -t $session:$window 'python -m venv python3-virtualenv' C-m
#tmux send-keys -t $session:$window 'source python3-virtualenv/bin/activate' C-m
#tmux send-keys -t $session:$window 'pip install -r requirements.txt' C-m
#tmux send-keys -t $session:$window 'export FLASK_ENV=development' C-m
#tmux send-keys -t $session:$window 'flask run --host=0.0.0.0' C-m

