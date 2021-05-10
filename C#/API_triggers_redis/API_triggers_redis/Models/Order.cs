using System;
using System.ComponentModel.DataAnnotations;

namespace API_triggers_redis.Models
{
    public class Order
    {
        [Key]
        public int Id { get; set; }

        [Required]
        public int UserId { get; set; }

        [Required]
        public int ProductId { get; set; }

        [Required]
        [Range(1, 1000, ErrorMessage = "Amount must be 1-1000")]
        public int Amount { get; set; }

        [Required]
        public DateTime Date { get; set; }



    }
}
