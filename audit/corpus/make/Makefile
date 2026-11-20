#@ mk.comment comment comment
# comment
#@ mk.var.def globalvar CC
#@ mk.assign.op quietop :=
CC := arm-none-eabi-gcc
#@ mk.assign.cond quietop ?=
CFLAGS ?= -O2
#@ mk.assign.append quietop +=
#@ mk.recipe.flag member -Wall
CFLAGS += -Wall
#@ mk.fn.builtin libfn wildcard
SRCS := $(wildcard src/*.c)
#@ mk.fn.patsubst libfn patsubst
OBJS := $(patsubst %.c,%.o,$(SRCS))

#@ mk.phony keyword .PHONY
.PHONY: all clean

#@ mk.target function all
#@ mk.prereq function app.elf
all: app.elf

#@ mk.var.use globalvar $(OBJS)
app.elf: $(OBJS)
#@ mk.var.use.recipe globalvar $(CC)
#@ mk.auto.target hazard $@
#@ mk.auto.all hazard $^
	$(CC) -o $@ $^

#@ mk.pattern.percent hazard %
%.o: %.c
#@ mk.auto.first hazard $<
#@ mk.var.braced globalvar ${CFLAGS}
	$(CC) ${CFLAGS} -c $< -o $@

#@ mk.cond.ifeq keyword ifeq
ifeq ($(OS),Windows_NT)
RM := del
#@ mk.cond.endif keyword endif
endif

#@ mk.include keyword include
-include deps.mk

#@ mk.define keyword define
define banner
@echo building
endef

clean:
	$(RM) $(OBJS) app.elf

ifeq ($(V),1)
Q :=
#@ mk.else keyword else
else
Q := @
endif
#@ mk.vpath keyword vpath
vpath %.c src
#@ mk.continuation escape \
LONG := a \
        b
