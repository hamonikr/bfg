#!/usr/bin/env python3

import subprocess
import argparse
import os
import sys
import logging

logging.basicConfig(level=logging.INFO)

def download_bfg():
    try:
        bfg_path = os.path.expanduser("~/bin/bfg.jar")
        if not os.path.exists(bfg_path):
            logging.info("Downloading bfg.jar...")
            subprocess.run(["curl", "-o", bfg_path, "https://repo1.maven.org/maven2/com/madgag/bfg/1.14.0/bfg-1.14.0.jar"], check=True)
        return bfg_path
    except Exception as e:
        logging.error(f"Failed to download bfg.jar: {e}")
        sys.exit(1)

def clone_repo(repo_url):
    try:
        logging.info("Cloning repository...")
        repo_url = repo_url.rstrip('.git') + '.git'
        subprocess.run(["git", "clone", "--mirror", repo_url, f"{repo_url}.git"], check=True)
    except Exception as e:
        logging.error(f"Failed to clone repository: {e}")
        sys.exit(1)

def find_big_files(size, repo_path):
    try:
        logging.info(f"Finding big files larger than {size}M...")
        subprocess.run(["java", "-jar", download_bfg(), f"--strip-blobs-bigger-than {size}M", "--no-blob-protection", repo_path], check=True)
    except Exception as e:
        logging.error(f"Failed to find big files: {e}")
        sys.exit(1)

def remove_big_files(size, repo_path):
    try:
        logging.info(f"Removing big files larger than {size}M...")
        subprocess.run(["java", "-jar", download_bfg(), f"--strip-blobs-bigger-than {size}M", repo_path], check=True)
        subprocess.run(["git", "reflog", "expire", "--expire=now", "--all"], check=True)
        subprocess.run(["git", "gc", "--prune=now", "--aggressive"], check=True)
    except Exception as e:
        logging.error(f"Failed to remove big files: {e}")
        sys.exit(1)

def push_changes(repo_path):
    try:
        logging.info("Pushing changes to remote...")
        subprocess.run(["git", "-C", repo_path, "push"], check=True)
    except Exception as e:
        logging.error(f"Failed to push changes: {e}")
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="Manage Git repositories.")
    parser.add_argument("--clone", dest="repo_url", help="Clone the specified Git repository.")
    parser.add_argument("--find-big-files", dest="find_size", help="Find files larger than the specified size in the repository.")
    parser.add_argument("--remove-big-files", dest="remove_size", help="Remove files larger than the specified size from the repository.")
    parser.add_argument("--push", dest="push", action="store_true", help="Push the changes to the remote repository.")
    parser.add_argument("repo_path", nargs="?", help="Path to the repository.")
    args = parser.parse_args()

    if args.repo_url:
        clone_repo(args.repo_url)
    if args.find_size:
        find_big_files(args.find_size, args.repo_path)
    if args.remove_size:
        remove_big_files(args.remove_size, args.repo_path)
    if args.push:
        push_changes(args.repo_path)

if __name__ == "__main__":
    main()
