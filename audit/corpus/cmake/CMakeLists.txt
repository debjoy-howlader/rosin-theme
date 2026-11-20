#@ cm.comment comment comment
# comment
#@ cm.cmd function cmake_minimum_required
#@ cm.kwarg qualifier VERSION
#@ cm.number number 3.20
cmake_minimum_required(VERSION 3.20)
#@ cm.cmd.project function project
project(blink C ASM)

#@ cm.cmd.set function set
#@ cm.var.name globalvar BOARD
#@ cm.string string esp32
set(BOARD "esp32")
#@ cm.var.cache.kw qualifier CACHE
#@ cm.bool number ON
set(USE_LOG ON CACHE BOOL "enable logging")

#@ cm.kw.if keyword if
#@ cm.var.use globalvar ${BOARD}
#@ cm.op.strequal quietop STREQUAL
if(${BOARD} STREQUAL "esp32")
  #@ cm.env globalvar $ENV{IDF_PATH}
  message(STATUS "IDF at $ENV{IDF_PATH}")
#@ cm.kw.endif keyword endif
endif()

#@ cm.fn.def.kw keyword function
#@ cm.fn.def.name function add_fw
function(add_fw name)
  #@ cm.cmd.add_executable function add_executable
  add_executable(${name} src/main.c)
  #@ cm.kwarg.public qualifier PRIVATE
  #@ cm.genex.open hazard $<
  target_compile_definitions(${name} PRIVATE $<$<CONFIG:Debug>:DEBUG=1>)
endfunction()

#@ cm.user.call function add_fw
add_fw(blink)
#@ cm.prop member C_STANDARD
set_target_properties(blink PROPERTIES C_STANDARD 11)
#@ cm.bracket.arg string bracket
message([[bracket argument]])
#@ cm.foreach keyword foreach
foreach(src IN LISTS SRCS)
endforeach()
#@ cm.comment.bracket comment bracket
#[[ bracket comment ]]
#@ cm.escape escape \n
message("line\n")
function(f2)
  #@ cm.return keyword return
  return()
endfunction()
#@ cm.cache.var globalvar $CACHE{
message("$CACHE{BOARD}")
#@ cm.cmd.prop function get_property
get_property(v GLOBAL PROPERTY X)
