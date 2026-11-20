/*@ ld.comment comment comment */
/* comment */
/*@ ld.cmd.entry keyword ENTRY */
/*@ ld.entry.symbol function Reset_Handler */
ENTRY(Reset_Handler)

/*@ ld.memory keyword MEMORY */
MEMORY
{
  /*@ ld.region.name composite FLASH */
  /*@ ld.region.attr qualifier rx */
  /*@ ld.origin keyword ORIGIN */
  /*@ ld.number number 0x08000000 */
  /*@ ld.size.suffix unit ~K */
  FLASH (rx) : ORIGIN = 0x08000000, LENGTH = 512K
  RAM (rwx)  : ORIGIN = 0x20000000, LENGTH = 128K
}

/*@ ld.sections keyword SECTIONS */
SECTIONS
{
  /*@ ld.section.name composite .text */
  .text :
  {
    /*@ ld.keep.2 keyword KEEP */
    KEEP(*(.isr_vector))
    *(.text*)
    /*@ ld.align keyword ALIGN */
    . = ALIGN(4);
    /*@ ld.symbol.def globalvar _etext */
    /*@ ld.location.counter hazard . */
    _etext = .;
  /*@ ld.region.use composite FLASH */
  } > FLASH
}

/*@ ld.phdrs keyword PHDRS */
PHDRS { text PT_LOAD; }
/*@ ld.discard composite /DISCARD/ */
SECTIONS { /DISCARD/ : { *(.comment) } }
/*@ ld.provide keyword PROVIDE */
PROVIDE(_heap = 0x20001000);
/*@ ld.number.dec number 4096 */
_stack_size = 4096;
/* ---- pass 1b coverage additions ---- */
/*@ ld.keep.2 keyword KEEP */
/*@ ld.datatype keyword LONG */
/*@ ld.align.2 keyword ALIGN */
SECTIONS { .isr2 : { KEEP(*(.isr_vector2)) LONG(0) . = ALIGN(4); } > FLASH }
