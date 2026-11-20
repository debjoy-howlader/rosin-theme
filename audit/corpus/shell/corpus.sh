#!/usr/bin/env bash
#@ sh.comment comment comment
# comment
#@ sh.var.assign globalvar PORT
#@ sh.string string ttyUSB0
PORT="/dev/ttyUSB0"
#@ sh.kw.qualifier.local qualifier export
#@ sh.var.assign.export globalvar BAUD
#@ sh.number number 115200
export BAUD=115200

#@ sh.fn.decl function flash
flash() {
    #@ sh.kw.local qualifier local
    local fw="$1"
    #@ sh.builtin libfn echo
    #@ sh.var.use globalvar $PORT
    #@ sh.var.positional hazard $1
    echo "flashing $1 to $PORT"
    #@ sh.cmd function esptool
    #@ sh.flag.long member --port
    #@ sh.var.braced globalvar ${PORT}
    #@ sh.flag.short member -b
    #@ sh.arg.plain variable write_flash
    esptool --port "${PORT}" -b "$BAUD" write_flash 0x0 "$fw"
}

#@ sh.kw.if keyword if
#@ sh.test.open punct [[
#@ sh.flag.test member -f
#@ sh.kw.then keyword then
if [[ -f build/app.bin ]]; then
    #@ sh.fn.call function flash
    flash build/app.bin
#@ sh.kw.fi keyword fi
fi

#@ sh.kw.for keyword for
#@ sh.kw.in keyword in
#@ sh.subst.open punct $(
for f in $(ls *.bin); do
    #@ sh.var.default globalvar ${f
    #@ sh.param.op quietop :-
    echo "${f:-none}"
#@ sh.kw.done keyword done
done

#@ sh.special hazard $?
#@ sh.redirect quietop >
#@ sh.redirect.fd quietop 2>&1
status=$? ; ls missing > /dev/null 2>&1
#@ sh.pipe quietop |
#@ sh.cmd.grep function grep
#@ sh.op.and keyword &&
dmesg | grep tty && echo found
#@ sh.arith.num number 2
n=$(( status + 2 ))
#@ sh.heredoc.delim directive EOF
cat <<EOF
#@ sh.heredoc.body string text
heredoc text
EOF
#@ sh.case keyword case
#@ sh.esac keyword esac
case "$PORT" in *USB*) echo usb ;; esac
#@ sh.single.string string single
echo 'single quoted'
#@ sh.backtick punct `
d=`date`

# ---- coverage additions ----
#@ sh.kw.function keyword function
#@ sh.fn.decl.kw function reset
function reset { :; }
#@ sh.alias.kw keyword alias
#@ sh.alias.name function ll
alias ll='ls -l'
#@ sh.while keyword while
#@ sh.arith.op quietop <
i=0; while (( i < 3 )); do i=$((i+1)); done
#@ sh.array.assign globalvar arr
#@ sh.array.paren punct (
arr=(a b c)
#@ sh.array.access globalvar ${arr
#@ sh.array.at hazard @
echo "${arr[@]}" "${#arr[@]}"
#@ sh.herestring quietop <<<
#@ sh.herestring.body string here
grep x <<< "here"
#@ sh.procsubst string <(
diff <(ls) <(ls -a)
#@ sh.ansi.string string ~$'
#@ sh.ansi.escape escape \t
printf $'tab\there\n'
#@ sh.or.op keyword ||
#@ sh.background punct &
true || false; sleep 1 &
#@ sh.glob hazard *
#@ sh.tilde quietop ~
ls ~/*.txt
#@ sh.case.default quietop *)
case $1 in a) ;; *) ;; esac
#@ sh.select keyword select
select opt in a b; do break; done
#@ sh.env.prefix globalvar LANG
LANG=C sort file
#@ sh.redirect.stdout quietop >>
echo x >> log.txt
#@ sh.escape escape \"
echo "say \"hi\""
#@ sh.number.octal number 0755
chmod 0755 f
#@ sh.declare qualifier declare
declare -i count=0
#@ sh.while.kw keyword while
while read -r line; do echo "$line"; done < input.txt
#@ sh.extglob hazard @(
shopt -s extglob; ls @(a|b).txt ?(x) +(y)
#@ sh.regex.match quietop =~
[[ $x =~ ^[0-9]+$ ]]
#@ sh.subshell punct (
( cd /tmp && ls )
#@ sh.group punct {
{ echo a; echo b; }
#@ sh.local.readonly qualifier readonly
readonly CONST=1
#@ sh.heredoc.quoted directive END
cat <<'END'
quoted heredoc $NOEXPAND
END
#@ sh.args.all hazard $@
printf '%s\n' "$@"
#@ sh.array.append globalvar arr
arr+=(d)
#@ sh.escape.hex escape \x41
#@ sh.escape.octal escape \033
echo $'\x41\033[0m\cA'
#@ sh.line.continuation escape \
echo one \
  two
#@ sh.clobber quietop >|
echo x >| out.txt
#@ sh.semicolon.range punct ;;
case a in a) echo ;; esac
#@ sh.number.decimal number 42
exit 42

# ---- pass 1b coverage additions ----
#@ sh.for.kw keyword for
#@ sh.for.var globalvar f
#@ sh.for.in keyword in
for f in *.c; do echo "$f"; done
#@ sh.cfor.kw keyword for
for ((j = 0; j < 3; j++)); do :; done
#@ sh.number.decimal2 number 42
(( k = 42 ))
#@ sh.version.arg number ~1.2.3
pip install pkg==1.2.3
#@ sh.assoc.decl qualifier declare
declare -A m; m[key]=v; echo "${m[key]}"
#@ sh.fn.call.user function reset
reset
#@ sh.cmd.quoted function "ls"
"ls" -l
#@ sh.arith.single punct $[
echo $[1 + 1]
#@ sh.regex.group punct (
[[ $x =~ (a|b)+ ]]
#@ sh.or.sep keyword ||
grep -q x file || echo missing
#@ sh.tilde.cd quietop ~
cd ~
    # indented comment
#@ sh.redirect.out quietop >
echo y > out.txt
#@ sh.redirect.both quietop &>
make &> build.log
#@ sh.until keyword until
until false; do break; done
