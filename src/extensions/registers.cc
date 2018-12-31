//
// Copyright (c) 2018 Bryson Lee. All rights reserved.
//
// A Meyers singleton that mocks a set of 1024 32-bit
// device registers located at 0xD0000000.
//

#include <stdexcept>

#include "registers.hh"

void Registers::set( uint32_t reg, uint32_t val )
{
  if ( (reg < base_) || (reg >= base_+sizeof(regs_)/sizeof(uint32_t)) )
    throw std::runtime_error( "invalid register access" );
  regs_[reg - base_] = val;
};

uint32_t Registers::get( uint32_t reg ) const
{
  if ( (reg < base_) || (reg >= base_+sizeof(regs_)/sizeof(uint32_t)) )
    throw std::runtime_error( "invalid register access" );
  return regs_[reg - base_];
};
