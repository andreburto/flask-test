describe("The initial test.", () => {
    beforeEach(() => {
        cy.request("PUT", "/reset")
    })

    it("First test", () => {
        cy.visit("/", { timeout: 5000 })
        cy.contains("value")
        cy.contains("0")
    })

    it("Increment test", () => {
        cy.request("PUT", "/inc")
        cy.wait(1000)
        cy.visit("/")
        cy.contains("value")
        cy.contains("1")
    })

    it("Decrement test", () => {
        cy.request("PUT", "/dec")
        cy.wait(1000)
        cy.visit("/")
        cy.contains("value")
        cy.contains("-1")
    })

    it("Up and down test", () => {
        cy.request("PUT", "/inc/2")
        cy.wait(1000)
        cy.visit("/")
        cy.contains("2")

        cy.request("PUT", "/dec/3")
        cy.wait(1000)
        cy.visit("/")
        cy.contains("-1")
    })
})