//
//
//

#include <cmath>
#include <stdexcept>

#include "fan.hh"

Fan::Fan()
{
}

Fan::~Fan()
{
}

void Fan::set_speed( double pctspeed )
{
  // make sure requested speed is 0-100%...
  if ( (0.0 > pctspeed) || (100.0 < pctspeed) )
    throw std::runtime_error( "requested speed must be in [0.0,100.0]%" );
  
  do_set_speed( pctspeed );
}

double Fan::get_speed()
{
  return do_get_speed();
}

std::string Fan::get_name() const
{
  return do_get_name();
}

PWM_Fan::PWM_Fan( const std::string& name, uint32_t pwm_max, uint32_t pwm_addr, double rpm_max ) :
  name_(name), pwm_max_(pwm_max), pwm_addr_(pwm_addr), rpm_max_(rpm_max), pwm_(0)
{
}

PWM_Fan::~PWM_Fan()
{
}

void PWM_Fan::do_set_speed( double pctspeed )
{
  pwm_ = std::lround( (double) pwm_max_ * pctspeed / 100.0 );
}

double PWM_Fan::do_get_speed()
{
  return (double) pwm_ / (double) pwm_max_ * rpm_max_;
}

std::string PWM_Fan::do_get_name() const
{
  return name_;
}


