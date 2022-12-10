# Advent of Code 2022

## Getting Started
With [Python](https://www.python.org/downloads/) installed locally and [VSCode Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python), you can run the solutions inside VSCode.

I'm running Python 3.11.

## Progress
### 2022
* [x] Day One
* [x] Day Two
  * [x] alt approach
* [x] Day Three
  * [x] alt approach
* [x] Day Four
  * [x] alt approach
* [x] Day Five
* [x] Day Six
* [ ] Day Seven - late!
* [ ] Day Eight - late!
* [ ] Day Nine - gonna be late

### Prep
Working through some 2021 puzzles to shake the dust off my python.
* [x] Day One
* [x] Day Two
* [x] Day Three
* [ ] Day Four

## Resources
* https://adventofcode.com/

### Python
* https://docs.python.org/3.10/
* https://code.visualstudio.com/docs/python/python-tutorial
* https://docs.python-guide.org/writing/structure/
* https://realpython.com/documenting-python-code/#docstring-types

---

## VM Stuff
Before I realized VS Code could run solutions, I was running them in a VM.

### Running

```
$ cd <folder-with-Vagrantfile>
$ vagrant up      # run VM
$ vagrant ssh     # enter VM
vagrant:~$ exit   # exit VM
$ vagrant halt    # shut down VM
```

### Updating

```
$ vagrant box update              # update box
vagrant:~$ do-release-upgrade     # update the OS
vagrant:~$ sudo apt-get update    # update apt-get
```

### Resources
* https://medium.com/@botdotcom/installing-virtualbox-and-vagrant-on-windows-10-2e5cbc6bd6ad
  * os: ubuntu/focal64
* https://developer.hashicorp.com/vagrant/tutorials/getting-started/getting-started-project-setup
* vim commands: https://vim.rtorr.com/
* https://realpython.com/vim-and-python-a-match-made-in-heaven/
