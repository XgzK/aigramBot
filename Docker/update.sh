#!/usr/bin/env bash

dir_tmp="/aigramBot"
## 更新机器人
update_aigramBot() {
  # shellcheck disable=SC2155
  local githubStatus=$(curl -s -m 2 -IL "https://google.com" | grep 200)
  rm -rf ${dir_tmp}
  cd /
  # shellcheck disable=SC2236
  if [[ ! -z $githubStatus ]]; then
    echo -e "github.com...\n"
    git clone https://github.com/XgzK/aigramBot.git
    cd ${dir_tmp} || exit
    return
  else
    echo -e "mirror.ghproxy.com...\n"
    git clone https://mirror.ghproxy.com/https://github.com/XgzK/aigramBot.git
    status_code=$?
    if [ $status_code -eq 0 ]; then
      echo "克隆成功。退出"
      cd ${dir_tmp} || exit
      return
    fi
    echo -e "gitclone.com...\n"
    git clone https://gitclone.com/github.com/XgzK/aigramBot.git
    status_code=$?
    if [ $status_code -eq 0 ]; then
      echo "克隆成功。退出"
      cd ${dir_tmp} || exit
      return
    fi
    echo -e "dl.ghpig.top...\n"
    git clone https://dl.ghpig.top/https://github.com/XgzK/aigramBot.git
    status_code=$?
    if [ $status_code -eq 0 ]; then
      echo "克隆成功。退出"
      cd ${dir_tmp} || exit
      return
    fi
    echo -e "gh.con.sh...\n"
    git clone https://gh.con.sh/https://github.com/XgzK/aigramBot.git
    status_code=$?
    if [ $status_code -eq 0 ]; then
      echo "克隆成功。退出"
      cd ${dir_tmp} || exit
      return
    fi
    echo -e "sciproxy.com...\n"
    git clone https://sciproxy.com/github.com/XgzK/aigramBot.git
    status_code=$?
    if [ $status_code -eq 0 ]; then
      echo "克隆成功。退出"
      cd ${dir_tmp} || exit
      return
    fi
    echo -e "ghproxy.cc...\n"
    git clone https://ghproxy.cc/https://github.com/XgzK/aigramBot.git
    status_code=$?
    if [ $status_code -eq 0 ]; then
      echo "克隆成功。退出"
      cd ${dir_tmp} || exit
      return
    fi
    echo -e "cf.ghproxy.cc...\n"
    git clone https://cf.ghproxy.cc/https://github.com/XgzK/aigramBot.git
    status_code=$?
    if [ $status_code -eq 0 ]; then
      echo "克隆成功。退出"
      cd ${dir_tmp} || exit
      return
    fi
    echo -e "gh.jiasu.in...\n"
    git clone https://gh.jiasu.in/https://github.com/XgzK/aigramBot.git
    status_code=$?
    if [ $status_code -eq 0 ]; then
      echo "克隆成功。退出"
      cd ${dir_tmp} || exit
      return
    fi
    echo -e "ghproxy.com...\n"
    git clone https://ghproxy.com/https://github.com/XgzK/aigramBot.git
    status_code=$?
    if [ $status_code -eq 0 ]; then
      echo "克隆成功。退出"
      cd ${dir_tmp} || exit
      return
    fi
    echo -e "ghproxy.net...\n"
    git clone https://ghproxy.net/https://github.com/XgzK/aigramBot.git
    status_code=$?
    if [ $status_code -eq 0 ]; then
      echo "克隆成功。退出"
      cd ${dir_tmp} || exit
      return
    fi
    echo -e "download.incept.pw...\n"
    git clone https://download.incept.pw/XgzK/aigramBot.git
    status_code=$?
    if [ $status_code -eq 0 ]; then
      echo "克隆成功。退出"
      cd ${dir_tmp} || exit
      return
    fi
    echo -e "slink.ltd...\n"
    git clone https://slink.ltd/https://github.com/XgzK/aigramBot.git
    status_code=$?
    if [ $status_code -eq 0 ]; then
      echo "克隆成功。退出"
      cd ${dir_tmp} || exit
      return
    fi
  fi
}
update_aigramBot
