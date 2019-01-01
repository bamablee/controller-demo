//
// Copyright (c) 2018 Bryson Lee. All rights reserved.
//

#include <cmath>

#include "fan.hh"
#include "registers.hh"

PWM_Fan::PWM_Fan( const std::string& name, uint32_t pwm_max, uint32_t pwm_addr, double rpm_max ) :
  Actuator(name), pwm_max_(pwm_max), pwm_addr_(pwm_addr), rpm_max_(rpm_max), pwm_(0)
{
}

PWM_Fan::~PWM_Fan()
{
}

void PWM_Fan::do_write( double pctspeed )
{
  pwm_ = std::lround( (double) pwm_max_ * pctspeed / 100.0 );
  Registers::instance().set( pwm_addr_, pwm_ );
}

double PWM_Fan::do_read()
{
  return (double) pwm_ / (double) pwm_max_ * rpm_max_;
}


