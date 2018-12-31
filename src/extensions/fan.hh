//
// Copyright (c) 2018 Bryson Lee. All rights reserved.
//

#include <string>
#include <cstdint>

class Fan
{
public:
  virtual ~Fan();

  // public interface methods for users
  void set_speed( double pctspeed );
  double get_speed();
  std::string get_name() const;

  // forbid copying...
  Fan( Fan const & ) = delete;
  Fan & operator=( Fan const & ) = delete;

protected:
  // allow construction only in derived classes
  Fan();

private:
  // private methods for derived classes
  virtual void do_set_speed( double pctspeed ) = 0;
  virtual double do_get_speed() = 0;
  virtual std::string do_get_name() const = 0;
  
};

class PWM_Fan : public Fan
{
public:
  PWM_Fan( const std::string& name,
	   uint32_t pwm_max,
	   uint32_t pwm_addr,
	   double   rpm_max );

  virtual ~PWM_Fan();

private:
  void do_set_speed( double pctspeed ) final;
  double do_get_speed() final;
  std::string do_get_name() const final;

  std::string name_;
  uint32_t pwm_max_;
  uint32_t pwm_addr_;
  double   rpm_max_;

  uint32_t pwm_;

};
