#!/bin/bash

_bfg() {
    local cur prev opts
    COMPREPLY=()
    cur="${COMP_WORDS[COMP_CWORD]}"
    prev="${COMP_WORDS[COMP_CWORD-1]}"
    opts="--clone --find-big-files --remove-big-files --push --help"

    if [[ ${prev} == "--find-big-files" || ${prev} == "--remove-big-files" ]]; then
        # 파일 크기 자동완성 (예: 1M, 5M, 10M 등)
        COMPREPLY=( $(compgen -W "1M 5M 10M 50M 100M 500M 1G" -- ${cur}) )
        return 0
    elif [[ ${cur} == -* ]]; then
        # 옵션 자동완성
        COMPREPLY=( $(compgen -W "${opts}" -- ${cur}) )
        return 0
    else
        # 경로 자동완성
        COMPREPLY=( $(compgen -f ${cur}) )
        return 0
    fi
}

complete -F _bfg bfg
