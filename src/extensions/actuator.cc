//
// Copyright (c) 2018 Bryson Lee. All rights reserved.
//

#include <stdexcept>

#include "actuator.hh"

Actuator::Actuator( const std::string& name) : name_(name)
{
}

void Actuator::write( double pct_output )
{
  // make sure requested output is 0-100%...
  if ( (0.0 > pct_output) || (100.0 < pct_output) )
    throw std::runtime_error( "requested output must be in [0.0,100.0]%" );
  
  do_write( pct_output );
}

double Actuator::read()
{
  return do_read();
}

std::string Actuator::name() const
{
  return name_;
}

