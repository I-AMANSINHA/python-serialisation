<H1> gRPC V/S REST API V/S WEBHOOK </H1>

<p> gRPC </p>
- Use gRPC for the high-speed communication between your internal backend systems where low latency is critical.
- Scenario: Your frontend API needs to instantly verify if an item is in stock before letting a customer check out.

<p> REST API </P>
- Use a traditional REST API for the standard, public-facing action where a client explicitly requests a one-time change.
- Scenario: The customer clicks "Buy Now" on the checkout page, sending user data and payment details to the server.

<P> WEBHOOK </P> 
- Use a Webhook to let a third-party delivery service automatically notify your application when the status changes, without making your app constantly ask for updates.
- Scenario: The shipping carrier updates the package status to "Out for Delivery," which automatically alerts your main application.
