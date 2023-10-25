#!/usr/bin/env python3

import gi
import threading
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

import bfg_cli


class GitManagerWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Git Repository Manager")

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(vbox)

        self.repo_url_entry = Gtk.Entry()
        self.repo_url_entry.set_placeholder_text("Repository URL")
        vbox.pack_start(self.repo_url_entry, True, True, 0)

        clone_button = Gtk.Button(label="Clone")
        clone_button.connect("clicked", self.on_clone_clicked)
        vbox.pack_start(clone_button, True, True, 0)

        self.find_size_entry = Gtk.Entry()
        self.find_size_entry.set_placeholder_text("Find files bigger than")
        vbox.pack_start(self.find_size_entry, True, True, 0)

        find_button = Gtk.Button(label="Find")
        find_button.connect("clicked", self.on_find_clicked)
        vbox.pack_start(find_button, True, True, 0)

        self.remove_size_entry = Gtk.Entry()
        self.remove_size_entry.set_placeholder_text("Remove files bigger than")
        vbox.pack_start(self.remove_size_entry, True, True, 0)

        remove_button = Gtk.Button(label="Remove")
        remove_button.connect("clicked", self.on_remove_clicked)
        vbox.pack_start(remove_button, True, True, 0)

        self.repo_path_entry = Gtk.Entry()
        self.repo_path_entry.set_placeholder_text("Repository Path")
        vbox.pack_start(self.repo_path_entry, True, True, 0)

        push_button = Gtk.Button(label="Push Changes")
        push_button.connect("clicked", self.on_push_clicked)
        vbox.pack_start(push_button, True, True, 0)

    def on_clone_clicked(self, button):
        repo_url = self.repo_url_entry.get_text()
        threading.Thread(target=clone_repo, args=(repo_url,)).start()

    def on_find_clicked(self, button):
        size = self.find_size_entry.get_text()
        repo_path = self.repo_path_entry.get_text()
        threading.Thread(target=find_big_files, args=(size, repo_path)).start()

    def on_remove_clicked(self, button):
        size = self.remove_size_entry.get_text()
        repo_path = self.repo_path_entry.get_text()
        threading.Thread(target=remove_big_files, args=(size, repo_path)).start()

    def on_push_clicked(self, button):
        repo_path = self.repo_path_entry.get_text()
        threading.Thread(target=push_changes, args=(repo_path,)).start()

win = GitManagerWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
