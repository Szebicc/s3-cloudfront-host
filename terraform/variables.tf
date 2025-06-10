variable "region" {
  default = "eu-west-2"
  type = string
}

variable "price_class" {
    default = "PriceClass_100"
    type = string
    description = "availability for the host, set to 'All' if needed"
}
